todo_list = [0] * 10
command = input()
while command != "End":
    priority, note = command.split("-")
    priority = int(priority)
    index = priority - 1
    todo_list[index] = note
    command = input()
print([el for el in todo_list if el != 0])