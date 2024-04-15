def password_validator(x):
    is_digit = 0
    no_special_chars = False
    more_than_2_digits = False
    correct_lenght = False
    for el in x:
        if not el.isalnum() and not el.isspace():
            print("Password must consist only of letters and digits")
        else:
            no_special_chars = True
        if el.isdigit():
            is_digit += 1
    if 6 > len(x) or len(x) > 10:
        print("Password must be between 6 and 10 characters")
    else:
        correct_lenght = True
    if is_digit < 2:
        print("Password must have at least 2 digits")
    else:
        more_than_2_digits = True

    if more_than_2_digits and correct_lenght and no_special_chars:
        print("Password is valid")


string = input()
password_validator(string)
