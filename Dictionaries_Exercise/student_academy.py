n = int(input())
students = {}
for _ in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)


for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")
