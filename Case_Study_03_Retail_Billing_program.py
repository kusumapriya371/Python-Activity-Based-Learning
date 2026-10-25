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
