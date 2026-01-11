from itertools import combinations_with_replacement

# Read input
s, k = input().split()
k = int(k)

# Sort the string to ensure lexicographic order
s = ''.join(sorted(s))

# Generate combinations with replacement
for combo in combinations_with_replacement(s, k):
    print(''.join(combo))
