command = input()
prohibited_name = False
while True:
    if command == "Welcome!":
        break

    name = command

    if name == "Voldemort":
        print("You must not speak of that name!")
        prohibited_name = True
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    command = input()

if not prohibited_name:
    print("Welcome to Hogwarts.")
