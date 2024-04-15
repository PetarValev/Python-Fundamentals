import sys
n = int(input())
best_weight, best_time, best_quality = 0, 0, 0
best_snowball = -sys.maxsize
for _ in range(1, n + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_snowball = (weight / time) ** quality
    if current_snowball > best_snowball:
        best_snowball = current_snowball
        best_weight, best_time, best_quality = weight, time, quality


print(f"{best_weight} : {best_time} = {int(best_snowball)} ({best_quality})")