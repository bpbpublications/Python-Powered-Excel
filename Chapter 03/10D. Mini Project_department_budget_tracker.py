# ── Data ───────────────────────────────────────────────────────
expenses = [
    {"dept": "Marketing",   "category": "Ads",      "amount": 52000, "month": "Jan"},
    {"dept": "Marketing",   "category": "Events",   "amount": 38000, "month": "Feb"},
    {"dept": "Engineering", "category": "Software", "amount": 91000, "month": "Jan"},
    {"dept": "Engineering", "category": "Hardware", "amount": 47000, "month": "Feb"},
    {"dept": "HR",          "category": "Training", "amount": 23000, "month": "Jan"},
    {"dept": "HR",          "category": "Hiring",   "amount": 61000, "month": "Feb"},
    {"dept": "Sales",       "category": "Travel",   "amount": 34000, "month": "Jan"},
    {"dept": "Sales",       "category": "Gifts",    "amount": 18000, "month": "Feb"},
]

budgets = {
    "Marketing":   80000,
    "Engineering": 120000,
    "HR":          70000,
    "Sales":       60000,
}


# ── Function 1 ───────────────────────────────────────────────────────
# Like SUMIF: add up amounts grouped by department

def total_by_dept(expenses):
    totals = {}                          # start with empty dict
    for record in expenses:
        dept   = record["dept"]
        amount = record["amount"]

        if dept not in totals:
            totals[dept] = 0            # first time seeing this dept
        totals[dept] += amount

    return totals                        # {"Marketing": 90000, ...}


totals = total_by_dept(expenses)
print(totals)

# ── Function 2 ───────────────────────────────────────────────────────
# Like IF + conditional formatting: flag each dept as over/under budget

def budget_status(totals, budgets):
    print("--- Budget Status ---")
    for dept in totals:
        spent  = totals[dept]
        limit  = budgets[dept]
        gap    = spent - limit           # positive = over, negative = under

        if gap > 0:
            print(f"{dept:<12}: ₹{spent:,} spent of ₹{limit:,}  ⚠ OVER BUDGET by ₹{gap:,}")
        else:
            print(f"{dept:<12}: ₹{spent:,} spent of ₹{limit:,}  ✓ Under budget  (₹{abs(gap):,} remaining)")


budget_status(totals, budgets)

# ── Function 3 ───────────────────────────────────────────────────────
# Like MAX+MATCH: find which dept spent the most
# Key concept: max() accepts a lambda to define what "maximum" means

def highest_spender(totals):
    top_dept = max(totals, key=lambda dept: totals[dept])
    #                         ↑ lambda tells max() to compare by VALUE,
    #                           not by dept name alphabetically
    return top_dept, totals[top_dept]

highest_spender(totals)


# ── Main: wire all 4 functions together ──────────────────────────────

def main():
    totals = total_by_dept(expenses)

    print("\n===== DEPARTMENT BUDGET REPORT =====\n")

    print("--- Total Spend by Department ---")
    for dept, amount in totals.items():
        print(f"{dept:<12}:  ₹{amount:,}")

    print()
    budget_status(totals, budgets)

    print()
    dept, amount = highest_spender(totals)
    print("--- Highest Spender ---")
    print(f"{dept} spent the most: ₹{amount:,}")


# main()

# Safer way

if __name__ == "__main__": 
    main() 
