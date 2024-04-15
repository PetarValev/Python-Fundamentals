n = int(input())
full_room = False
free_chairs = 0
for room in range(1, n + 1):
    chairs, visitors = input().split()
    if len(chairs) < int(visitors):
        needed_chairs = int(visitors) - len(chairs)
        full_room = True
        print(f"{needed_chairs} more chairs needed in room {room}")
    elif len(chairs) > int(visitors):
        free_chairs += len(chairs) - int(visitors)

if not full_room:
    print(f"Game On, {free_chairs} free chairs left")