people = int(input())
capacity = int(input())
needed_trips = 0

while True:
    people -= capacity
    needed_trips += 1

    if people <= 0:
        break


print(needed_trips)
