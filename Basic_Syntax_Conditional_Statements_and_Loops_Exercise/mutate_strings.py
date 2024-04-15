string1 = input()
string2 = input()
result = string1
for idx in range(len(string1)):
    if string1[idx] == string2[idx]:
        continue
    result = string2[:idx + 1] + string1[idx + 1:]
    print(result)



