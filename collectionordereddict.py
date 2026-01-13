from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    data = input().split()
    price = int(data[-1])
    item_name = " ".join(data[:-1])

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item, total_price in items.items():
    print(item, total_price)
