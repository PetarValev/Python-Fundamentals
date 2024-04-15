elements = input().split()
bakery = {}


for i in range(0, len(elements), 2):
    item_index = i
    quantity_index = i + 1
    item = elements[item_index]
    quantity = int(elements[quantity_index])
    bakery[item] = quantity

print(bakery)