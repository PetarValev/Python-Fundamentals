command = input()
products = {}
while command != "statistics":
    item, quantity = command.split(":")
    if item not in products:
        products[item] = int(quantity)
    else:
        products[item] += int(quantity)

    command = input()

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")