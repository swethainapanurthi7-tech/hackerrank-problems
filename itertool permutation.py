from itertools import permutations

# Read input
s, k = input().split()
k = int(k)

# Sort the string to ensure lexicographic order
s = ''.join(sorted(s))

# Generate permutations of length k
perm = permutations(s, k)

# Print each permutation as a string
for p in perm:
    print(''.join(p))
