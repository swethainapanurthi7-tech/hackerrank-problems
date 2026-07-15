n = int(input())
a = input().split()
print(all(int(x) > 0 for x in a) and any(x == x[::-1] for x in a))
