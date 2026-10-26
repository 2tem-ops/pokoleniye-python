# Общие числа

nums1, nums2 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()])

print(*sorted(nums1 & nums2))