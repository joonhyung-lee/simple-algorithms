students = set(range(1, 31))
for _ in range(28):
    n = int(input())
    students.remove(n)

missing = sorted(students)
print(missing[0])
print(missing[1])