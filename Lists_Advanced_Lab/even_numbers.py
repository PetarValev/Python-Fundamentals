numbers = [int(x) for x in input().split(", ")]
even_numbers_indexes = [idx for idx in range(len(numbers)) if numbers[idx] % 2 == 0]
# for index, el in enumerate(numbers):
#     if el % 2 == 0:
#         even_numbers_indexes.append(index)
print(even_numbers_indexes)
