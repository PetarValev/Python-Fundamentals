numbers = [int(x) for x in input().split(", ")]


def some_func():
    for num in numbers:
        reversed_digit = list(reversed(str(num)))
        reversed_num = int(''.join(reversed_digit))
        if reversed_num == num:
            print("True")
        else:
            print("False")


some_func()
