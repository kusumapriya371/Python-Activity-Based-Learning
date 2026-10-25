# Warehouse Inventory Reconciliation
records = [
    ("Keyboard", 50, 20, 35, 34, 50),
    ("Mouse", 80, 10, 40, 50, 60),
    ("Monitor", 25, 5, 12, 18, 20),
]

print("WAREHOUSE RECONCILIATION")
for name, opening, incoming, dispatched, actual, target in records:
    if min(opening, incoming, dispatched, actual, target) < 0:
        print(name, "- INVALID: negative quantity")
    elif dispatched > opening + incoming:
        print(name, "- INVALID: dispatch exceeds available stock")
    else:
        expected = opening + incoming - dispatched
        discrepancy = actual - expected
        replenishment = max(0, target - actual)
        if discrepancy == 0:
            status = "MATCH"
        elif discrepancy < 0:
            status = "SHORTAGE"
        else:
            status = "SURPLUS"
        print(name, "Expected:", expected, "Actual:", actual,
              "Difference:", discrepancy, status,
              "Replenish:", replenishment)
