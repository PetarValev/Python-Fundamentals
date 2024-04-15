text = input()
fucked_chars = ["a", "o", "u", "e", "i"]
result = [el for el in text if el.lower() not in fucked_chars]
print("".join(result))

