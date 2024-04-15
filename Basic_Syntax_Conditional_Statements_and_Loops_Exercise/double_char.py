command = input()

while command != "End":
    if command != "SoftUni":
        for ch in command:
            print(ch * 2, end="")
        print()

    command = input()
#
# while True:
#     current_string = input()
#
#     if current_string == "End":
#         break
#
#     if current_string != "SoftUni":
#         result_string = ""
#         for char in current_string:
#             result_string += char * 2
#
#         print(result_string)
