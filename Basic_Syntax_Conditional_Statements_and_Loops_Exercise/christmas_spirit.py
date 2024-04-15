quantity_of_decoration = int(input())
days_until_christmas = int(input())
ornament_set_price = 2
skirt_price = 5
garland_price = 3
lights_price = 15
total_sum = 0
spirit = 0
for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decoration *= 2
    if day % 15 == 0:
        total_sum += quantity_of_decoration * (skirt_price + garland_price + lights_price)
        spirit += 47
    if day % 10 == 0:
        spirit -= 20
        total_sum += garland_price + skirt_price
    else:
        if day % 5 == 0:
            total_sum += quantity_of_decoration * lights_price
            spirit += 17
        if day % 3 == 0:
            total_sum += quantity_of_decoration * (skirt_price + garland_price)
            spirit += 13
        if day % 2 == 0:
            total_sum += quantity_of_decoration * ornament_set_price
            spirit += 5

if days_until_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {total_sum}")
print(f"Total spirit: {spirit}")

