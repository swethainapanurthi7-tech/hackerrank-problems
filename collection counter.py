from collections import Counter

# Number of shoes
n = int(input())

# Shoe sizes
shoe_sizes = Counter(map(int, input().split()))

# Number of customers
customers = int(input())

total_money = 0

for _ in range(customers):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        total_money += price
        shoe_sizes[size] -= 1

print(total_money)
