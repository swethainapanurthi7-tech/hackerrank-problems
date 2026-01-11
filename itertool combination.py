from itertools import combinations

# Read input
s, k = input().split()
k = int(k)

# Sort the string to ensure lexicographic order
s = ''.join(sorted(s))

# Generate combinations of length 1 to k
for i in range(1, k + 1):
    for combo in combinations(s, i):
        print(''.join(combo))
