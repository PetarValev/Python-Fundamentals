data = input()
telephone_book = {}

while "-" in data:
    data = data.split("-")
    for idx in range(0, len(data), 2):
        person = data[idx]
        number = data[idx + 1]
        telephone_book[person] = number

    data = input()

else:
    data = int(data)

for _ in range(data):
    name = input()
    if name not in telephone_book:
        print(f"Contact {name} does not exist.")

    else:
        print(f"{name} -> {telephone_book.get(name)}")