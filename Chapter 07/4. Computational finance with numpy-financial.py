import numpy_financial as npf

# 1. Monthly Loan Payment (PMT) ---------------------------
# To calculate the monthly payment (EMI) for 
# a ₹5,00,000 loan at 10% annual interest for 5 years.

# Loan details
principal = 500000
annual_rate = 0.10
years = 5

# Convert annual to monthly rate and term
monthly_rate = annual_rate / 12
n_months = years * 12

# Calculate EMI
emi = npf.pmt(rate=monthly_rate, nper=n_months, pv=-principal)
print(f"Monthly Payment (EMI): ₹{emi:,.2f}")

# Excel Equivalent =PMT(10%/12, 60, -500000)

# 2. Future Value of Investment (FV) ---------------------------
# Suppose you invest ₹5,000 every month for 10 years, 
# earning 8% annually. How much will you have at the end?

monthly_investment = 5000
annual_rate = 0.08
years = 10

monthly_rate = annual_rate / 12
n_months = years * 12

# Future value of recurring investments 
future_value = npf.fv(rate=monthly_rate, nper=n_months, pmt=-monthly_investment, pv=0)
print(f"Future Value: ₹{future_value:,.2f}")

# 3. Net Present Value (NPV) ---------------------------
# You expect a series of cash flows over 5 years:
# [-100000, 20000, 30000, 40000, 25000, 15000]
# (first value is Initial investment and rest are returns). 
# Initial investment = ₹1,00,000
# Returns over 5 years = ₹20k, ₹30k, ₹40k, ₹35k, ₹10k
# Assume a 10% discount rate.

cashflows = [-100000, 20000, 30000, 40000, 25000, 15000]
rate = 0.10

npv = npf.npv(rate, cashflows)
print(f"Net Present Value (NPV): ₹{npv:,.2f}")


# 4. Present Value (PV) ---------------------------
# Suppose you’ll receive ₹1,00,000 after 3 years. 
# What’s it worth today, at 8% annual interest?


future_value = 100000
rate = 0.08
n_years = 3

pv = npf.pv(rate=rate, nper=n_years, pmt=0, fv=-future_value)
print(f"Present Value: ₹{pv:,.2f}")


# Internal Rate of Return (IRR) ---------------------------
# What rate makes the NPV of cashflows = 0?
# Use the same cashflows as above:
    
irr = npf.irr(cashflows)
print(f"Internal Rate of Return (IRR): {irr * 100:.2f}%")

# NOTE: IRR may not always converge or return valid results for irregular cashflows.
# IRR results can vary slightly between Excel and Python.
# Excel uses a guess-based method and may return 0% if it fails to converge.
# Python’s npf.irr() uses a different algorithm and may yield a more accurate IRR
 # — but may also find a solution that Excel doesn't. 
 # Always cross-validate with NPV plots or alternative tools.

# If You Want an Aligned Result:
# You can manually verify IRR by plotting or solving for when NPV = 0 
# using a custom scipy.optimize code example to show IRR more robustly.    

# Next example
cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]
irr_value = npf.irr(cash_flows)

print(f"Internal Rate of Return (IRR): {irr_value:.6f}")

# CAGR (Compound Annual Growth Rate) ---------------------------
# What’s the average annual return between two values over a period?
# You invested ₹50,000 five years ago, and today it’s ₹80,000.
# NO LIBRARY NEEDED

start_value = 50000
end_value = 80000
years = 5

cagr = (end_value / start_value) ** (1 / years) - 1
print(f"CAGR: {cagr * 100:.2f}%")


# Warnings & Best Practices
# Always use positive values for inflows, and negative for outflows (just like Excel).
# Make sure to convert annual interest rates to monthly if payments are monthly.
# numpy-financial is a lightweight library — safe to use even in constrained environments.
