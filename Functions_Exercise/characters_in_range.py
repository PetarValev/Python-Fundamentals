def some_func(a, b):
    for el in range(ord(a) + 1, ord(b)):
        print(chr(el), end=" ")


first_char = input()
second_char = input()
some_func(first_char, second_char)

