from itertools import groupby

s = input().strip()

# Use groupby to compress consecutive characters
result = [(len(list(g)), int(k)) for k, g in groupby(s)]

# Print each tuple separated by space
print(*result)
