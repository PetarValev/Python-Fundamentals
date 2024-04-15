n = int(input())
counter = 0
prime = False
for n2 in range(1, n + 1):
    if n % n2 == 0:
        counter += 1

if counter == 2:
    prime = True


print(prime)
