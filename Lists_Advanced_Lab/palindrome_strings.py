# words = input().split()
# palindrome = input()
# palindromes = []
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)
#
# print(palindromes)
#
# counter = [el for el in words if el == palindrome]
# if len(counter) > 0:
#     print(f"Found palindrome {len(counter)} times")
# else:
#     print(f"Found palindrome 0 times")

strings = input().split()
searched_palindrome = input()
palindromes = [word for word in strings if word == ''.join(reversed(word))]

print(palindromes)
print(f'Found palindrome {palindromes.count(searched_palindrome)} times')


