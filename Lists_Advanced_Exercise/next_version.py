software_version = [int(x) for x in input().split(".")]

for index in range(len(software_version) - 1, -1, -1):
    if software_version[index] < 9:
        software_version[index] += 1
        break
    else:
        software_version[index] = 0
print(".".join([str(el) for el in software_version]))


