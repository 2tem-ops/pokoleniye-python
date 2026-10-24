# Больше предыдущего

nums = [int(i) for i in input().split()]
count = 0

for i in range(0, 1):
    for j in range(i + 1, len(nums)):
        if j > 1:
            i += 1
        if nums[j] > nums[i]:
            count += 1

print(count)