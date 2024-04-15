def calculate(product, quantity):
    if product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "coffee":
        price = 1.50
    else:
        price = 2.00
    return quantity * price


product_name = input()
quantity_of_product = int(input())
total_sum = calculate(product_name, quantity_of_product)

print(f"{total_sum:.2f}")
