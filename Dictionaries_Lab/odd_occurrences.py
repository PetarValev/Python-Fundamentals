info = input().lower().split()
wanted_words = {}
for el in info:
    if el in wanted_words:
        wanted_words[el] += 1
    else:
        wanted_words[el] = 1

for key, value in wanted_words.items():
    if value % 2 != 0:
        print(key, end=" ")

# words = [el.lower() for el in input().split()]
# default = 0
#
# occurs = dict.fromkeys(words, default)
#
# for el in words:
#     occurs[el] += 1
#
# for key, value in occurs.items():
#     if value % 2 != 0:
#         print(key, end=" ")