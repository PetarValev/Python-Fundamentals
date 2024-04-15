current_happy_year = int(input())
next_happy_year = current_happy_year + 1
while True:
    if len(str(current_happy_year)) == len(set(str(next_happy_year))):
        break
    else:
        next_happy_year += 1

print(next_happy_year)
