number = int(input())

for _ in range(number):
    string_is_pure = True
    string = input()
    for ch in string:
        if ch == "," or ch == "." or ch == "_":
            string_is_pure = False

    if string_is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")


