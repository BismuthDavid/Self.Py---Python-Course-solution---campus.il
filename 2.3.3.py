first_pig, second_pig, third_pig = input("Enter three digits (each digit for one pig)\n")
sum_of_bricks = int(first_pig) + int(second_pig) + int(third_pig)
print(sum_of_bricks)
print(sum_of_bricks // 3)
print(sum_of_bricks % 3)
sum_of_bricks = not bool(sum_of_bricks % 3)
print(sum_of_bricks)