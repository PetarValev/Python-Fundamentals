budget = int(input())
command = input()
budget_is_enough = True

while command != "End":
    current_price = int(command)
    budget -= current_price
    if budget < 0:
        budget_is_enough = False
        break

    command = input()


if budget_is_enough:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")

