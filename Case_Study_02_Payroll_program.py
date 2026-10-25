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
