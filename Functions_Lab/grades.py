def grade_receiver(gr):
    if 2.00 <= gr <= 2.99:
        return "Fail"
    elif 3.00 <= gr <= 3.49:
        return "Poor"
    elif 3.50 <= gr <= 4.49:
        return "Good"
    elif 4.50 <= gr <= 5.49:
        return "Very Good"
    else:
        return "Excellent"


grade_data = float(input())
result = grade_receiver(grade_data)
print(result)
