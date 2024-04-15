number = int(input())

for num in range(1, number + 1):
    str_to_num = str(num)
    total_sum = 0
    for digit in str_to_num:
        total_sum += int(digit)

    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
