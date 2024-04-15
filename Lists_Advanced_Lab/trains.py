train = [0 for _ in range(int(input()))]

command = input()

while command != "End":
    command_args = command.split()
    action = command_args[0]
    if action == "add":
        n_people = int(command_args[1])
        train[-1] += n_people
    elif action == "insert":
        index = int(command_args[1])
        n_people = int(command_args[2])
        train[index] += n_people
    elif action == "leave":
        index = int(command_args[1])
        n_people = int(command_args[2])
        train[index] -= n_people

    command = input()

print(train)