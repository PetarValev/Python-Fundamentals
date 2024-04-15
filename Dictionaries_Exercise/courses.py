data = input()
registered_students = {}
while data != "end":
    course_name, student_name = data.split(" : ")
    if course_name not in registered_students:
        registered_students[course_name] = []

    registered_students[course_name].append(student_name)

    data = input()

for course_name, student_name in registered_students.items():
    print(f"{course_name}: {len(student_name)}")
    for student in student_name:
        print(f"-- {student}")