#双色球
from random import randint

nums = []
for i in range(6):
    while True:
        num = randint(1,32)
        if num not in nums:
            nums.append(num)
            break
    blue = randint(1,15)

nums = sorted(nums)
nums.append(blue)
print(nums)