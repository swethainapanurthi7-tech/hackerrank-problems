# Number of English subscribers
n = int(input())
english = set(map(int, input().split()))

# Number of French subscribers
m = int(input())
french = set(map(int, input().split()))

# Union of both sets
total_students = english.union(french)

# Output the count
print(len(total_students))
