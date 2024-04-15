command = input()
total_coffee = 0
while True:
    if command == "END":
        break

    elif command == "movie" or command == "coding" or command == "dog" or command == "cat":
        total_coffee += 1
    elif command == "MOVIE" or command == "CODING" or command == "DOG" or command == "CAT":
        total_coffee += 2

    command = input()

if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)