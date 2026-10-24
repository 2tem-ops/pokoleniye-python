# Сдвиг в развитии

nums = input().split()
nums.insert(0, (nums.pop(-1)))
print(" ".join(nums))