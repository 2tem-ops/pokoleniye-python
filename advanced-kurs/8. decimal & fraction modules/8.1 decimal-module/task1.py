from decimal import Decimal as D

s = '0.0 5.42 8.63 10.25 1.6 -8.5 -13.0'

decimal_lst = [D(num) for num in s.split()]
print(max(decimal_lst) + min(decimal_lst))