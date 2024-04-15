courses = {}

info = input()

while ":" in info:
    student_name, student_id, course_name = info.split(":")
    if course_name not in courses:
        courses[course_name] = {student_id: student_name}
    else:
        courses[course_name][student_id] = student_name

    info = input()

course_name = " ".join(info.split("_"))
students = courses[course_name]

for key, value in students.items():
    print(f"{value} - {key}")
