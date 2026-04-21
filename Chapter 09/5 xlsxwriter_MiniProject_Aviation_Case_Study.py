import os
import datetime as dt
import xlsxwriter

wb = xlsxwriter.Workbook('xlsxwriter_Aviation_Case_Study.xlsx')

ws_flights   = wb.add_worksheet('Flights')     # main operational data
ws_routes    = wb.add_worksheet('Routes')      # simple route reference
ws_helper    = wb.add_worksheet('Helper')      # all calculations + normalized data
ws_dashboard = wb.add_worksheet('Dashboard')   # clean dashboard

# ----------------- Formats -----------------

fmt_header   = wb.add_format({'bold': True, 'bg_color': '#E4DFEC', 'border': 1, 'align': 'center'})
fmt_money    = wb.add_format({'num_format': '$#,##0', 'border': 1})
fmt_int      = wb.add_format({'num_format': '0', 'border': 1})
fmt_pct      = wb.add_format({'num_format': '0.0%', 'border': 1})
fmt_text     = wb.add_format({'border': 1})
fmt_date     = wb.add_format({'num_format': 'yyyy-mm-dd', 'border': 1})
fmt_warn     = wb.add_format({'bg_color': '#FFC7CE'})
fmt_title    = wb.add_format({'bold': True, 'font_size': 16, 
                              'bg_color': '#7030A0', 'font_color':'#FFFFFF',
                              'align': 'center',
                              'valign': 'vcenter'})

# ----------------- Flights Sheet -----------------

fl_hdrs = [
    'Flight_ID', 'Family', 'Aircraft_Type', 'Route',
    'Departure_Date', 'Seats', 'Load_Factor', 'Delay_Min', 'Passengers'
]
ws_flights.write_row(0, 0, fl_hdrs, fmt_header)

fl_rows = [
    ['F001', 'Airbus', 'A320',     'DEL–BOM', dt.date(2025, 8, 1), 180, 0.86,  8],
    ['F002', 'Boeing', 'B737-800', 'DEL–BLR', dt.date(2025, 8, 1), 189, 0.78, 17],
    ['F003', 'Airbus', 'A321',     'BOM–HYD', dt.date(2025, 8, 2), 220, 0.81,  2],
    ['F004', 'Boeing', 'B737-900', 'BLR–MAA', dt.date(2025, 8, 2), 220, 0.74, 25],
    ['F005', 'Airbus', 'A320',     'DEL–BOM', dt.date(2025, 8, 3), 180, 0.92,  3],
]

for r, row in enumerate(fl_rows, start=1):
    ws_flights.write(r, 0, row[0], fmt_text)                 
    ws_flights.write(r, 1, row[1], fmt_text)                 
    ws_flights.write(r, 2, row[2], fmt_text)                 
    ws_flights.write(r, 3, row[3], fmt_text)                 
    ws_flights.write_datetime(r, 4, row[4], fmt_date)        
    ws_flights.write(r, 5, row[5], fmt_int)                  
    ws_flights.write(r, 6, row[6], fmt_pct)                  
    ws_flights.write(r, 7, row[7], fmt_int)                  
    ws_flights.write_formula(r, 8, f"=ROUND(F{r+1}*G{r+1},0)", fmt_int)

## Autofilter, column width & Sparkline (for demo purpose)-----

ws_flights.autofilter(0, 0, len(fl_rows), 8)
ws_flights.set_column('A:A', 14)
ws_flights.set_column('B:E', 16)
ws_flights.set_column('F:I', 14)
ws_flights.set_column('J:J', 21)

ws_flights.write('J1', 'Load_Factor Trend', fmt_header)

ws_flights.add_sparkline('J2', {
    'range': 'Flights!G2:G10',  # Load_Factor values
    'type': 'line',
    'markers': True,
    'high_point': True,
    'style': 12
})


# Conditional Formatting --------------

last_data_row = 1 + len(fl_rows)

# G column _Load_Factor (Data starts from 2nd row)
ws_flights.conditional_format(1, 6, last_data_row, 6, {              
    'type': '3_color_scale'
})

# H column _Delay Min (Data starts from 2nd row)
ws_flights.conditional_format(1, 7, last_data_row, 7, {      
    'type': 'cell', 'criteria': '>', 'value': 15, 'format': fmt_warn
})

# ----------------- Routes Sheet -----------------

ws_routes.write_row('A1', ['Route', 'Distance_nm', 'Fuel_Burn_kg'], fmt_header)
routes = [
    ['DEL–BOM', 710, 2300],
    ['DEL–BLR', 1060, 3400],
    ['BOM–HYD', 390, 1600],
    ['BLR–MAA', 160, 900],
]
for r, row in enumerate(routes, start=1):
    ws_routes.write_row(r, 0, row)
ws_routes.set_column('A:B', 12)
ws_routes.set_column('C:C', 16)

# ----------------- Helper Sheet (all calculations) -----------------

# Per Route Data 
ws_helper.write_row('A1', ['Route', 'Passengers', 'Avg Delay', 'Route Efficiency Index'], fmt_header)

for i, r in enumerate(routes, start=0):
    ws_helper.write(1+i, 0, r[0], fmt_text)
    ws_helper.write_formula(1+i, 1,
        f"=SUMIF(Flights!D:D, A{2+i}, Flights!I:I)", fmt_int)
    ws_helper.write_formula(1+i, 2,
        f"=AVERAGEIF(Flights!D:D, A{2+i}, Flights!H:H)", fmt_int)
    ws_helper.write_formula(1+i, 3,
        f"=IFERROR((AVERAGEIF(Flights!D:D,A{2+i},Flights!G:G)*" +
        f"VLOOKUP(A{2+i},Routes!A:B,2,FALSE))/" +
        f"C{2+i}, \"\")", fmt_int)

# wb.define_name('tbl_RouteMetrics', '=Helper!$A$1:$D$5')

# Avg Load Factor + Remaining (for Doughnut Chart)
ws_helper.write('F1', 'Average Load Factor', fmt_header)
ws_helper.write_formula('F2', f"=AVERAGE(Flights!G2:G{last_data_row})", fmt_pct)

ws_helper.write('G1', 'Remaining', fmt_header)
ws_helper.write_formula('G2', f"=1-F2", fmt_pct)

# Normalized KPI table (for Radar Chart)
ws_helper.write_row('I1', ['Route', 'Eff_Index_Norm', 'Delay_Norm', 'LoadFactor_Norm'], fmt_header)
for i in range(len(routes)):
    ws_helper.write_formula(1+i, 8, f"=A{2+i}")  # Route
    ws_helper.write_formula(1+i, 9, f"=D{2+i}/MAX(D$2:D$5)*100")  # Eff norm
    ws_helper.write_formula(1+i, 10, f"=100-(C{2+i}/MAX(C$2:C$5)*100)")  # Delay norm (inverse)
    ws_helper.write_formula(1+i, 11, f"=AVERAGEIF(Flights!D:D,A{2+i},Flights!G:G)*100")  # LoadF norm


ws_helper.set_column('B:D', 20)
ws_helper.set_column('F:G', 21)
ws_helper.set_column('J:L', 18)

# ----------------- Dashboard Sheet (clean view) -----------------

# Asthetics ----------------------

ws_dashboard.set_tab_color('#7030A0')
ws_dashboard.merge_range('A1:L1', 'Aviation KPI Dashboard', fmt_title)
ws_dashboard.hide_gridlines(2)
ws_dashboard.set_row(0, 30)

# KPIs and logo ----------------------

ws_dashboard.write('C3', 'Total Fuel Burn (kg)', fmt_header)
ws_dashboard.write_formula('C4',
    '=SUMPRODUCT(SUMIFS(Routes!C2:C5, Routes!A2:A5, Flights!D2:D6))',
    fmt_money)

ws_dashboard.write('K3', 'Average Delay (Min)', fmt_header)
ws_dashboard.write('K4', f"=AVERAGE(Flights!H2:H{last_data_row})", fmt_int)

ws_dashboard.set_column('C:C', 20)
ws_dashboard.set_column('K:K', 20)
ws_dashboard.set_row(2, 26)
ws_dashboard.set_row(3, 23)

# Logo
logo_path = 'airbus.jpg'
if os.path.exists(logo_path):
    ws_dashboard.insert_image('G3', logo_path, {'x_scale': 0.8, 'y_scale': 0.6})


# Per Route Data(from helper sheet instead of computing again)
for r in range(5):          # 5 rows (A1:D5)
    for c in range(4):      # 4 cols (A1:D5)
        cell_ref = f"=Helper!{chr(65+c)}{r+1}"
        if r == 0:
            ws_dashboard.write_formula(r+21, c+7, cell_ref, fmt_header)
        else:
            ws_dashboard.write_formula(r+21, c+7, cell_ref, fmt_int)

ws_dashboard.set_column('I:J', 14)
ws_dashboard.set_row(21, 26)
for row in range(22, 26):  
    ws_dashboard.set_row(row, 23)
    
# Charts  ----------------------
        
# Chart 1: Combo chart Passengers vs Avg Delay --------

chart_combo = wb.add_chart({'type': 'column'})
chart_combo.add_series({
    'name':       'Passengers',
    'categories': ['Helper', 1, 0, 1+len(routes)-1, 0],
    'values':     ['Helper', 1, 1, 1+len(routes)-1, 1],
    'data_labels': {'value': True},
    'fill':       {'color': '#E4DFEC'}
})
chart_line = wb.add_chart({'type': 'line'})
chart_line.add_series({
    'name':       'Average Delay',
    'categories': ['Helper', 1, 0, 1+len(routes)-1, 0],
    'values':     ['Helper', 1, 2, 1+len(routes)-1, 2],
    'y2_axis':    False,
    'data_labels': {'value': True},
    'line': {'color': '#7030A0', 'width': 2},
    'marker': {
        'type': 'circle',       # Options: automatic, circle, square, diamond, triangle, x
        'size': 6,              # Marker size
        'border': {'color': '#7030A0'},
        'fill':   {'color': '#FFFFFF'}  # Optional: white fill for contrast
    }

})

chart_combo.combine(chart_line)
chart_combo.set_y_axis({'visible': False, 'major_gridlines': {'visible': False}})
chart_combo.set_title({'name': 'Passengers vs Average Delay', 'name_font': {'color': '#7030A0'}})
chart_combo.set_legend({'position': 'bottom'})
ws_dashboard.insert_chart('A6', chart_combo, {'x_offset': 15, 'y_offset': 10})

# Chart 2: Doughnut chart Avg Load Factor  --------

chart_l = wb.add_chart({'type': 'doughnut'})
chart_l.add_series({
    'categories': ['Helper', 0, 5, 0, 6],
    'values':     ['Helper', 1, 5, 1, 6],
    'points': [
        {'fill': {'color': '#7030A0'}},
        {'fill': {'color': '#E4DFEC'}},
    ],
    'data_labels': {'value': True}
})
chart_l.set_title({'name': 'Average Load Factor', 'name_font': {'color': '#7030A0'}})
chart_l.set_style(22)
chart_l.set_legend({'none': True})
ws_dashboard.insert_chart('A22', chart_l, {'x_offset': 15, 'y_scale': 0.6 })
chart_l.set_hole_size(35)   # default 50 
chart_l.set_chartarea({
    'border': {'none': True},
    'fill':   {'color': 'white'}  # blends with background
})


# Chart 3: Radar chart normalized KPIs  --------

chart_radar = wb.add_chart({'type': 'radar', 'subtype': 'filled'})
chart_radar.add_series({
    'name': 'Efficiency Index',
    'categories': ['Helper', 1, 8, 1+len(routes)-1, 8],
    'values':     ['Helper', 1, 9, 1+len(routes)-1, 9],
    'fill':   {'none': True},
    'border': {'color': '#7030A0'}
})
chart_radar.add_series({
    'name': 'Avg Delay (Norm)',
    'categories': ['Helper', 1, 8, 1+len(routes)-1, 8],
    'values':     ['Helper', 1, 10, 1+len(routes)-1, 10],
    'fill':   {'none': True},
    'border': {'color': '#FF3333'}
})
chart_radar.add_series({
    'name': 'Avg Load Factor',
    'categories': ['Helper', 1, 8, 1+len(routes)-1, 8],
    'values':     ['Helper', 1, 11, 1+len(routes)-1, 11],
    'fill':   {'none': True},
    'border': {'color': '#3366FF'}
})
chart_radar.set_title({'name': 'Efficiency vs Delay vs Load Factor (Normalized)', 'name_font': {'color': '#7030A0'}})
chart_radar.set_legend({'position': 'bottom'})
ws_dashboard.insert_chart('H6', chart_radar, {'y_offset': 10, 'x_scale': 0.9 })

# Chart 4: REI Column (You can adjust the placement)  --------
# chart_e = wb.add_chart({'type': 'column'})
# chart_e.add_series({
#     'categories': ['Helper', 1, 0, 1+len(routes)-1, 0],
#     'values':     ['Helper', 1, 3, 1+len(routes)-1, 3],
#     'data_labels': {'value': True},
#     'fill':       {'color': '#E4DFEC'}
# })
# chart_e.set_title({'name': 'Route Efficiency Index', 'name_font': {'color': '#7030A0'}})
# chart_e.set_style(22)
# chart_e.set_y_axis({'visible': False, 'major_gridlines': {'visible': False}})
# chart_e.set_legend({'none': True})
# ws_dashboard.insert_chart('M6', chart_e, {'x_offset': 15, 'y_offset': 10})


wb.close()
