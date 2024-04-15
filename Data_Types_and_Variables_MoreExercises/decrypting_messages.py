key = int(input())
n = int(input())
result = ""
for _ in range(n):
    char = input()
    char_to_ord = ord(char) + key
    result += chr(char_to_ord)

print(result)
