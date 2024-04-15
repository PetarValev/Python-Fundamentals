sequence_of_numbers = [int(x) for x in input().split()]


def some_func():
    min_number = min(sequence_of_numbers)
    max_number = max(sequence_of_numbers)
    total_sum = sum(sequence_of_numbers)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {total_sum}")


some_func()
