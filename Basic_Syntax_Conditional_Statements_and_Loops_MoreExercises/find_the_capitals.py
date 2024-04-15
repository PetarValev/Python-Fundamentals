string = str(input())
collection = []
for idx in range(len(string)):
    if string[idx].isupper():
        collection.append(idx)

print(collection)
