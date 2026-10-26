# Встречалось ли число раньше?

nums = [int(i) for i in input().split()]
nums_set = set()

for num in nums:
    print("YES" if num in nums_set else "NO")
    nums_set.add(num)