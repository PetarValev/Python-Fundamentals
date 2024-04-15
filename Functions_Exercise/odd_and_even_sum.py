def sum_nums(n):
    even_result = 0
    odd_result = 0
    for el in n:
        if int(el) % 2 == 0:
            even_result += int(el)
        else:
            odd_result += int(el)
    print(f"Odd sum = {odd_result}, Even sum = {even_result}")


number = input()
sum_nums(number)
