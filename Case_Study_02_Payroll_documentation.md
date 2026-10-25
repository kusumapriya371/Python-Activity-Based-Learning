# Case Study 02: Employee Payroll and Deduction Analysis

## 1. Problem Statement
Calculate employee gross salary from basic pay, allowances, overtime, and incentives. Apply progressive deductions and print a formatted salary statement.

## 2. Objectives
- Calculate gross earnings from salary components.
- Apply a simple progressive deduction policy.
- Display gross pay, deduction, and net pay clearly.

## 3. Assumptions
- HRA is 20% of basic pay and other allowance is 10%.
- Overtime is paid at ₹200 per hour and incentives are supplied directly.
- Illustrative deduction: 5% of gross up to ₹30,000; 10% of the amount above ₹30,000 up to ₹60,000; 15% of any amount above ₹60,000.

## 4. Algorithm
1. Read or define basic pay, overtime hours, and incentive.
2. Calculate allowances, overtime pay, and gross pay.
3. Calculate deduction in progressive bands.
4. Subtract deduction from gross pay.
5. Print a formatted salary statement.

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
INPUT basic pay, overtime hours, incentive
CALCULATE HRA = 20% of basic
CALCULATE other allowance = 10% of basic
CALCULATE gross = basic + allowances + overtime pay + incentive
CALCULATE deduction by progressive bands
CALCULATE net = gross - deduction
DISPLAY salary statement
```

## 7. Python Source Code
```python
# Employee Payroll and Deduction Analysis
basic = 28000
overtime_hours = 6
incentive = 2500

hra = basic * 0.20
other_allowance = basic * 0.10
overtime_pay = overtime_hours * 200
gross = basic + hra + other_allowance + overtime_pay + incentive

# Illustrative progressive deduction
deduction = 0
if gross > 60000:
    deduction = 30000 * 0.05 + 30000 * 0.10 + (gross - 60000) * 0.15
elif gross > 30000:
    deduction = 30000 * 0.05 + (gross - 30000) * 0.10
else:
    deduction = gross * 0.05

net = gross - deduction
print("EMPLOYEE SALARY STATEMENT")
print("Basic pay       : Rs.", round(basic, 2))
print("HRA             : Rs.", round(hra, 2))
print("Other allowance : Rs.", round(other_allowance, 2))
print("Overtime pay    : Rs.", round(overtime_pay, 2))
print("Incentive       : Rs.", round(incentive, 2))
print("Gross salary    : Rs.", round(gross, 2))
print("Deduction       : Rs.", round(deduction, 2))
print("Net salary      : Rs.", round(net, 2))
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Normal salary | Basic ₹28,000; overtime 6 hours; incentive ₹2,500 | Gross ₹40,100; deduction ₹2,510; net ₹37,590 |
| No overtime | Overtime hours = 0 | Overtime pay = ₹0 |
| Low gross | Gross ≤ ₹30,000 | Deduction = 5% of gross |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program demonstrates salary component calculations and progressive deductions. The rates are academic assumptions, not legal payroll or tax advice.
