# healthcare_udfs.py

import pandas as pd
import xlwings as xw


# Utility function to load and prepare merged dataset


def get_data():
    """Loads and merges patients, encounters, providers from the Excel file."""
    book = xw.Book.caller()
    path = getattr(book, "fullpath", book.fullname)

    patients = pd.read_excel(path, sheet_name='patients')
    encounters = pd.read_excel(path, sheet_name='encounters')
    providers = pd.read_excel(path, sheet_name='providers')

    merged = (
        encounters
        .merge(patients, on='patient_id', how='left')
        .merge(providers, on='provider_id', how='left')
    )

    # Convert date columns to datetime for filtering/aggregation
    merged['encounter_date'] = pd.to_datetime(merged['encounter_date'], errors='coerce')
    return patients, encounters, providers, merged


# UDFs to analyze data -------------------------

# Avg encounter cost by department


@xw.func
def avg_cost_by_department(department):
    """
    Returns average encounter cost for a given department.
    Usage: =avg_cost_by_department("Primary Care")
    """
    _, _, _, df = get_data()
    subset = df[df['department'].str.lower() == department.lower()]
    if subset.empty:
        return "No data"
    return round(subset['cost_usd'].mean(), 2)



# Monthly revenue (optionally filter by year)

@xw.func
@xw.arg('year', doc="Year to filter (e.g., 2024). Leave blank for all years.")
@xw.ret(expand='table', index=False)
def monthly_revenue(year=None):
    """
    Returns monthly total revenue.
    Usage:
      =monthly_revenue()       → all months
      =monthly_revenue(2024)   → only for year 2024
    """
    _, _, _, df = get_data()
    df = df.dropna(subset=['encounter_date', 'cost_usd'])

    # Create year-month
    df['year'] = df['encounter_date'].dt.year
    df['month'] = df['encounter_date'].dt.to_period('M').astype(str)

    if year is not None:
        df = df[df['year'] == int(year)]

    result = (
        df.groupby('month', as_index=False)['cost_usd']
          .sum()
          .rename(columns={'cost_usd': 'total_revenue_usd'})
          .sort_values('month')
    )

    return result


# Recent encounters (filterable) Will be a useful function only if data is recent

@xw.func
@xw.ret(expand='table', index=False)
def recent_encounters(city=None, department=None, days=30):
    """
    Returns encounters in the last N days, optionally filtered by city/department.
    Usage:
      =recent_encounters()
      =recent_encounters("Madison", "Cardiology", 30)
    """
    _, _, _, df = get_data()

    today = pd.Timestamp.today()
    cutoff = today - pd.Timedelta(days=int(days))

    # Apply filters dynamically
    mask = df['encounter_date'] >= cutoff
    if city:
        mask &= df['city'].str.lower().eq(city.lower())
    if department:
        mask &= df['department'].str.lower().eq(department.lower())

    subset = df.loc[
        mask,
        [
            'encounter_id', 'patient_id', 'encounter_date', 'department',
            'provider_id', 'length_of_stay_days', 'cost_usd', 'outcome'
        ]
    ].sort_values('encounter_date', ascending=False)

    if subset.empty:
        return [["No data"]]

    # Return with headers
    return subset



# Readmission rate by department


@xw.func
@xw.ret(expand='table', index=False)
def readmission_rate_by_department():
    """
    Returns department-level 30-day readmission summary.
    Usage: =readmission_rate_by_department()
    """
    _, _, _, df = get_data()

    grouped = (
        df.groupby('department', dropna=True)
          .agg(readmits=('readmission_30', 'sum'),
               encounters=('encounter_id', 'count'))
          .reset_index()
    )
    grouped['readmit_rate'] = (100 * grouped['readmits'] / grouped['encounters']).round(2)

    return grouped



# Top N providers by number of encounters

@xw.func
@xw.ret(expand='table', index=False)
def top_providers(n=10):
    """
    Returns top N providers by number of encounters.
    Usage: =top_providers(10)
    """
    _, _, _, df = get_data()

    grouped = (
        df.groupby(['provider_id', 'provider_name', 'specialty'], dropna=True)
          .agg(encounters_count=('encounter_id', 'count'),
               avg_cost_usd=('cost_usd', 'mean'))
          .reset_index()
          .sort_values('encounters_count', ascending=False)
          .head(int(n))
    )
    grouped['avg_cost_usd'] = grouped['avg_cost_usd'].round(2)

    return grouped



# Patient summary (aggregated view)


@xw.func
@xw.ret(expand='table', index=False)
def patient_summary(patient_id):
    """
    Returns a summary for a specific patient ID.
    Columns: total_encounters, last_encounter_date, total_cost, avg_cost, readmissions_30
    Usage: =patient_summary(123)
    """
    _, _, _, df = get_data()

    subset = df[df['patient_id'] == int(patient_id)]
    if subset.empty:
        return [["No data"]]

    summary = {
        'total_encounters': subset.shape[0],
        'last_encounter_date': subset['encounter_date'].max().strftime('%Y-%m-%d'),
        'total_cost': round(subset['cost_usd'].sum(), 2),
        'avg_cost': round(subset['cost_usd'].mean(), 2),
        'readmissions_30': int(subset['readmission_30'].sum())
    }

    # Convert dict to Excel-friendly table
    result = pd.DataFrame(summary, index=[0])
    return result
