# Number of students subscribed to English newspaper
n = int(input())
english = set(map(int, input().split()))

# Number of students subscribed to French newspaper
m = int(input())
french = set(map(int, input().split()))

# Students who subscribed only to English
only_english = english.difference(french)

# Output the count
print(len(only_english))
