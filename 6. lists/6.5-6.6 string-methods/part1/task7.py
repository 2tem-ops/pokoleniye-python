# Количество совпадающих пар

n = input()

nums = n.split()
pairs = 0

for i in range(len(nums)):
    for j in range(1 + i, len(nums)):
        if nums[i] == nums[j]:
            pairs += 1

print(pairs)