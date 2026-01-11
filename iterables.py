from itertools import combinations
from math import comb

# Read input
n = int(input())
letters = input().split()
k = int(input())

# Count occurrences of 'a'
count_a = letters.count('a')
count_non_a = n - count_a

# Handle case when k > count_non_a to avoid negative combinations
if k > count_non_a:
    prob_no_a = 0
else:
    prob_no_a = comb(count_non_a, k) / comb(n, k)

# Probability of at least one 'a'
prob_at_least_one_a = 1 - prob_no_a

# Print with 4 decimal places as HackerRank expects
print(f"{prob_at_least_one_a:.4f}")
