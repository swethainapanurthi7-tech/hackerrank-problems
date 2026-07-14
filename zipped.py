n, x = map(int, input().split())

marks = []

for _ in range(x):
    marks.append(list(map(float, input().split())))

for student in zip(*marks):
    print(sum(student) / x)
