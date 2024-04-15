command = input()
products = {}

while command != "buy":
    data = command.split()
    name = data[0]
    price = float(data[1])
    quantity = int(data[2])
    if name not in products:
        products[name] = []
        products[name].append(price)
        products[name].append(quantity)
    else:
        products[name][0] = price
        products[name][1] += quantity

    command = input()

for key, value in products.items():
    result = value[0] * value[1]
    print(f"{key} -> {result:.2f}")