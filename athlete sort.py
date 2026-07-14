n, m = map(int, input().split())

data = [input().split() for _ in range(n)]

k = int(input())

data.sort(key=lambda row: int(row[k]))

for row in data:
    print(*row)
