# number = int(input())
#
# for _ in range(number):
#     current_number = int(input())
#     if current_number != 88 and current_number != 86:
#         if current_number < 88:
#             print("GREAT!")
#         else:
#             print("Bye.")
#     elif current_number == 88:
#         print("Hello")
#     else:
#         print("How are you?")

number = int(input())

for _ in range(number):
    current_number = int(input())
    if current_number == 88:
        print("Hello")
    elif current_number == 86:
        print("How are you?")
    else:
        if current_number < 88:
            print("GREAT!")
        else:
            print("Bye.")