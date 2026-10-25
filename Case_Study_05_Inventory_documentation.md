# Case Study 05: Warehouse Inventory Reconciliation

## 1. Problem Statement
Reconcile opening stock, incoming stock, dispatched stock, and physically counted closing stock for multiple products. Identify discrepancies and calculate replenishment needs against target stock.

## 2. Objectives
- Calculate expected closing stock.
- Detect differences between expected and actual stock.
- Calculate replenishment needed to reach target stock.

## 3. Assumptions
- Each record is a tuple: product, opening, incoming, dispatched, actual closing, target stock.
- All quantities must be non-negative integers.
- Expected closing = opening + incoming − dispatched.

## 4. Algorithm
1. Read product records.
2. Validate quantities and prevent negative expected stock.
3. Calculate expected closing and compare it with actual closing.
4. Calculate discrepancy as actual minus expected.
5. Calculate replenishment as max(0, target minus actual).
6. Display reconciliation report.

## 5. Flowchart
```text
START
  |
LOAD INPUT / SAMPLE DATA
  |
VALIDATE INPUTS
  |
PROCESS USING CONDITIONS AND LOOPS
  |
DISPLAY RESULTS AND ERRORS
  |
END
```

## 6. Pseudocode
```text
FOR each product record
  IF any quantity is negative or dispatched > opening + incoming
    DISPLAY invalid record
  ELSE
    expected = opening + incoming - dispatched
    discrepancy = actual - expected
    replenishment = maximum(0, target - actual)
    DISPLAY result
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Matching stock | Opening 50, incoming 20, dispatched 35, actual 35 | Expected 35; difference 0 |
| Stock shortage | Expected 35, actual 34 | Difference -1; shortage |
| Invalid dispatch | Opening 10, incoming 2, dispatched 15 | Invalid: dispatch exceeds available stock |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program compares theoretical and physical stock, flags discrepancies, and estimates replenishment quantities.
