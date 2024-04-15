number = int(input())
number_to_string = str(number)
result = "".join(sorted(number_to_string, reverse=True))
print(int(result))

# number = input()
# for n in range(9, -1, -1):
#     for i in number:
#         if int(i) == int(n):
#             print(n, end="")