command = input()
resources = {}
while command != "stop":
    material = command
    quantity = int(input())
    if material in resources:
        resources[material] += quantity
    else:
        resources[material] = quantity

    command = input()

for key, value in resources.items():
    print(f"{key} -> {value}")