students = []

n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Get unique grades and sort them
grades = sorted(set(student[1] for student in students))

# Second lowest grade
second_lowest = grades[1]

# Get names with the second lowest grade
names = [student[0] for student in students if student[1] == second_lowest]

# Sort names alphabetically
names.sort()

# Print result
for name in names:
    print(name)
