def calculator(operator, first_num, second_num):
    result = 0
    if operator == "multiply":
        result = first_num * second_num
    elif operator == "divide":
        result = first_num // second_num
    elif operator == "subtract":
        result = first_num - second_num
    else:
        result = first_num + second_num
    return result


print(calculator(input(), int(input()), int(input())))


