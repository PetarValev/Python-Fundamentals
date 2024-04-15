score = [int(x) for x in input().split()]
factor = int(input())
score = [x * factor for x in score]
total_sum =[x for x in score if x >= sum(score) / len(score)]
if len(total_sum) >= len(score) / 2:
    print(f"Score: {len(total_sum)}/{len(score)}. Employees are happy!")
else:
    print(f"Score: {len(total_sum)}/{len(score)}. Employees are not happy!")

