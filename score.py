n = int(input())
scores = list(map(int, input().split()))

# Remove duplicates and sort
unique_scores = list(set(scores))
unique_scores.sort()

# Print runner-up score
print(unique_scores[-2])
