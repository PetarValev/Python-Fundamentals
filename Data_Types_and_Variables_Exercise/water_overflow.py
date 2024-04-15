n = int(input())
water_tank = 255
total_litters = 0
for _ in range(n):
    litters = int(input())
    if water_tank - litters < 0:
        print("Insufficient capacity!")
    else:
        water_tank -= litters
        total_litters += litters


print(total_litters)

