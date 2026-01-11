n, m = map(int, input().split())

# Top part
for i in range(1, n, 2):
    pattern = ".|." * i
    print(pattern.center(m, "-"))

# Middle part
print("WELCOME".center(m, "-"))

# Bottom part (mirror of top)
for i in range(n - 2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(m, "-"))
