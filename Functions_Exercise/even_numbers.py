sequence_of_numbers = [int(x) for x in input().split()]


def some_func(x):
    if x % 2 == 0:
        return True
    else:
        return False


even_nums = list(filter(some_func, sequence_of_numbers))
print(even_nums)
