from collections import defaultdict

n, m = map(int, input().split())

positions = defaultdict(list)

# Read Group A
for i in range(1, n + 1):
    word = input().strip()
    positions[word].append(i)

# Read Group B and print results
for _ in range(m):
    word = input().strip()
    if word in positions:
        print(*positions[word])
    else:
        print(-1)