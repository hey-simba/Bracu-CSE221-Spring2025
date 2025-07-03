n = int(input())
id = input().strip().split()
id = list(map(int, id))
marks = input().strip().split()
marks = list(map(int, marks))

students = []
for i in range(n):
    students.append([id[i], marks[i]])

swap = 0

for i in range(n):
    max_idx = i

    for j in range(i + 1, n):

        if (students[j][1] > students[max_idx][1]) or (students[j][1] == students[max_idx][1] and students[j][0] < students[max_idx][0]):
            max_idx = j


    if max_idx != i:
        students[i], students[max_idx] = students[max_idx], students[i]
        swap += 1


print(f"Minimum swaps: {swap}")
for student in students:
    print(f"ID: {student[0]} Mark: {student[1]}")