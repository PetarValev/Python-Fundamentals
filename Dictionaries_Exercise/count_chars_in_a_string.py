data = input().split()
info = {}

for word in data:
    for letter in word:
        if letter not in info:
            info[letter] = 1
        else:
            info[letter] += 1

for key, value in info.items():
    print(f"{key} -> {value}")