# Назад, вперед и наоборот

nums = input().split()

if len(nums) > 1:
    for i in range(0, len(nums), 2):
        k = i + 1
        if k == len(nums):
            break
        nums[i], nums[k] = nums[k], nums[i]

print(" ".join(nums))

# 2 3 2 4 5