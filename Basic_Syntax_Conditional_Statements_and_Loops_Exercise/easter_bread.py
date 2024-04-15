budget = float(input())
price_for_one_kg_floor = float(input())
pack_of_eggs = price_for_one_kg_floor * 0.75
one_litter_milk = price_for_one_kg_floor * 1.25
total_sum_for_loaf = price_for_one_kg_floor + pack_of_eggs + (one_litter_milk / 4)
total_loaves = 0
easter_eggs = 0

while True:
    if budget - total_sum_for_loaf > 0:
        budget -= total_sum_for_loaf
        easter_eggs += 3
        total_loaves += 1
    else:
        break

    if total_loaves % 3 == 0:
        easter_eggs = easter_eggs - (total_loaves - 2)


print(f"You made {total_loaves} loaves of Easter bread! Now you have {easter_eggs} eggs and {budget:.2f}BGN left.")

