info = input().split()
stocks = {}
for i in range(0, len(info), 2):
    item = info[i]
    quantity = int(info[i + 1])
    stocks[item] = quantity


searched_products = input().split()

for current_product in searched_products:
    if current_product not in stocks:
        print(f"Sorry, we don't have {current_product}")
    else:
        print(f"We have {stocks.get(current_product)} of {current_product} left")