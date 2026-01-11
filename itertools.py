from itertools import product

# Read input lists
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute Cartesian product
result = product(A, B)

# Print as space-separated tuples
print(*result)
