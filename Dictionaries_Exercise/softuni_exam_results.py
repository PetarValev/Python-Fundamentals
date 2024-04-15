data = input()
exam_results = {}
while data != "exam finished":
    username, language, points = data.split("-")
    exam_results[language] = {}
    if username not in exam_results[language]:
        exam_results[language][username] = int(points)
    else:
        exam_results[language][username] += int(points)
    data = input()
print(exam_results)
