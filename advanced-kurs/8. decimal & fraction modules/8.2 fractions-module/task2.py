from fractions import Fraction as F

s = '0.21 74.5 12.3 -11.77 48.6542 114.55'

nums = [F(num) for num in s.split()]
print(max(nums) + min(nums))