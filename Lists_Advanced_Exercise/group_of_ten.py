numbers = [int(x) for x in input().split(", ")]
group = 10
while len(numbers) > 0:
    current_group = [num for num in numbers if num <= group]
    print(f"Group of {group}'s: {current_group}")
    for num in current_group:
        if num in numbers:
            numbers.remove(num)

    current_group.clear()
    group += 10

