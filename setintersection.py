# Number of students subscribed to English newspaper
n = int(input())
english = set(map(int, input().split()))

# Number of students subscribed to French newspaper
m = int(input())
french = set(map(int, input().split()))

# Find students subscribed to both
both = english.intersection(french)

# Output the count
print(len(both))
