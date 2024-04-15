n = int(input())

for rows in range(1, n + 1):
    for cols in range(1, rows + 1):
        print("*", end='')
    print()

for rows in range(n, 1, -1):
    for cols in range(rows, 1, -1):
        print("*", end='')
    print()
