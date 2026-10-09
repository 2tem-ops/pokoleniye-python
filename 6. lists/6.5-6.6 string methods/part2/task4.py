# Переставить min и max

s = input().split()

nums = []

for num in s:
    nums.append(int(num))

maximum = nums.index(max(nums))
minimum = nums.index(min(nums))

s[maximum], s[minimum] = s[minimum], s[maximum]

print(" ".join(s))
