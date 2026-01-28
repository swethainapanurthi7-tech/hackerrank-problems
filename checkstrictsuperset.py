A = set(map(int, input().split()))
n = int(input())

is_strict = True

for _ in range(n):
    other = set(map(int, input().split()))
    if not (A > other):
        is_strict = False
        break

print(is_strict)
