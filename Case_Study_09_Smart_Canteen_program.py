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
