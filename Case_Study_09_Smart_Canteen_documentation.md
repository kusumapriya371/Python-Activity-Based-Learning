# Case Study 09: Smart Canteen Order and Stock Management

## 1. Problem Statement
Process a sequence of canteen orders, calculate bills, update inventory, reject orders that exceed available stock, and summarize sales and remaining stock.

## 2. Objectives
- Maintain product stock in lists.
- Validate order quantities before accepting an order.
- Calculate sales and report remaining stock.

## 3. Assumptions
- Each order is a tuple of product name and quantity.
- Prices and initial stock are supplied in parallel lists.
- Only positive quantities and known product names are accepted.

## 4. Algorithm
1. Define menu items, prices, stock, and sample orders.
2. For each order, locate the product.
3. Reject unknown products, non-positive quantities, or quantities exceeding stock.
4. Otherwise calculate bill, reduce stock, and add to total sales.
5. Display each order result and final stock.

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
SET menu, prices, stock, and orders
SET total_sales = 0
FOR each order
  FIND product index
  IF not found, reject
  ELSE IF quantity <= 0, reject
  ELSE IF quantity > stock, reject
  ELSE calculate bill, reduce stock, add bill to sales
DISPLAY total sales and remaining stock
```

## 7. Python Source Code
```python
# Smart Canteen Order and Stock Management
menu = ["Idli", "Dosa", "Sandwich", "Juice"]
prices = [30, 50, 70, 40]
stock = [40, 25, 15, 20]
orders = [
    ("Idli", 4),
    ("Dosa", 2),
    ("Sandwich", 20),  # rejected: insufficient stock
    ("Juice", 3),
    ("Unknown", 1),    # rejected: not on menu
]

total_sales = 0
for product, quantity in orders:
    if product not in menu:
        print("REJECTED:", product, "- product not found")
    elif quantity <= 0:
        print("REJECTED:", product, "- quantity must be positive")
    else:
        index = menu.index(product)
        if quantity > stock[index]:
            print("REJECTED:", product, "- insufficient stock")
        else:
            bill = prices[index] * quantity
            stock[index] -= quantity
            total_sales += bill
            print("ACCEPTED:", product, "Qty:", quantity,
                  "Bill: Rs.", bill)

print("\nTotal sales: Rs.", total_sales)
print("REMAINING STOCK")
for i in range(len(menu)):
    print(menu[i], ":", stock[i])
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Valid order | Idli quantity 4; stock 40 | Accepted; bill ₹120; stock becomes 36 |
| Insufficient stock | Sandwich quantity 20; stock 15 | Rejected; stock unchanged |
| Unknown item | Product 'Unknown' | Rejected: product not found |
| Invalid quantity | Quantity 0 | Rejected: quantity must be positive |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program simulates order processing, stock control, and daily sales using lists, tuples, loops, and conditional statements.
