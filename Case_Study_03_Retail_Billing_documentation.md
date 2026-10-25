# Case Study 03: Retail Billing with Multiple Discount Rules

## 1. Problem Statement
Prepare an itemized retail invoice for multiple products, quantities, category-specific tax rates, threshold discounts, and a maximum discount limit.

## 2. Objectives
- Calculate each product line total.
- Apply a threshold discount without exceeding the discount cap.
- Calculate category taxes and the final invoice amount.

## 3. Assumptions
- Each item is represented as a tuple: name, unit price, quantity, tax rate percentage.
- A 10% discount applies when pre-tax subtotal is at least ₹5,000, capped at ₹1,000.
- Taxes are calculated after discount, proportionally across the taxable subtotal.

## 4. Algorithm
1. Read product tuples and calculate line totals.
2. Add line totals to subtotal.
3. Calculate discount based on threshold and cap.
4. Calculate taxable subtotal after discount.
5. Apply each product's tax rate to its discounted line share.
6. Display invoice totals.

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
SET products list
SET subtotal = 0
FOR each product tuple
  CALCULATE line total and add to subtotal
IF subtotal >= 5000, discount = minimum(10% of subtotal, 1000), ELSE discount = 0
CALCULATE discount ratio = discount / subtotal
FOR each product, reduce line by discount ratio and calculate tax
DISPLAY lines, subtotal, discount, tax, and final total
```

## 7. Python Source Code
```python
# Retail Billing with Multiple Discount Rules
products = [
    ("Notebook", 120, 10, 5),
    ("Backpack", 1200, 3, 12),
    ("Pen set", 250, 4, 5),
]

subtotal = 0
for name, price, quantity, tax_rate in products:
    subtotal += price * quantity

if subtotal >= 5000:
    discount = min(subtotal * 0.10, 1000)
else:
    discount = 0

discount_ratio = discount / subtotal if subtotal > 0 else 0
total_tax = 0
print("ITEMIZED INVOICE")
for name, price, quantity, tax_rate in products:
    line_total = price * quantity
    discounted_line = line_total * (1 - discount_ratio)
    tax = discounted_line * tax_rate / 100
    total_tax += tax
    print(name, "Qty:", quantity, "Line:", round(line_total, 2),
          "Tax:", round(tax, 2))

final_total = subtotal - discount + total_tax
print("Subtotal      : Rs.", round(subtotal, 2))
print("Discount      : Rs.", round(discount, 2))
print("Total tax     : Rs.", round(total_tax, 2))
print("Final payable : Rs.", round(final_total, 2))
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Above threshold | Sample basket subtotal ₹5,800 | 10% discount = ₹580, below the ₹1,000 cap |
| Below threshold | Subtotal ₹4,000 | Discount ₹0 |
| Empty basket | No products | Subtotal and final total are ₹0; no division error |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program creates an itemized invoice and demonstrates list processing, loops, conditional discounts, and tax calculations.
