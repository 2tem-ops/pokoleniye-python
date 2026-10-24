# Произведение чисел

n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

product = int(input())

count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] * nums[j] == product:
            count += 1

if count >= 1:
    print("ДА")
else:
    print("НЕТ")
