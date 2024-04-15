n = int(input())
register = {}
for _ in range(n):
    data = input().split()
    command = data[0]
    if command == "register":
        name = data[1]
        license_plate = data[2]
        if name not in register:
            register[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    else:
        name = data[1]
        if name not in register:
            print(f"ERROR: user {name} not found")
        else:
            del register[name]
            print(f"{name} unregistered successfully")


for name, plate in register.items():
    print(f"{name} => {plate}")