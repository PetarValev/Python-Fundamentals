# a = input().split(", ")
# b = input().split(", ")
# result = []
# for el in a:
#     for elem in b:
#         if el in elem:
#             result.append(el)
#             break
#
# print(result)

def find_substrings(a, b):
    substrings = [s1 for s1 in first if any(s1 in s2 for s2 in second)]
    print(substrings)


first = input().split(", ")
second = input().split(", ")

find_substrings(first, second)