group_size = int(input())
days = int(input())
total_coins = 0

for current_day in range(1, days + 1):
    total_coins += 50 - (group_size * 2)
    if current_day % 15 == 0:
        group_size += 5
        total_coins -= group_size * 2
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 5 == 0:
        total_coins += group_size * 20
    if current_day % 3 == 0:
        total_coins -= group_size * 3

final_coins = total_coins // group_size
print(f"{group_size} companions received {final_coins} coins each.")
