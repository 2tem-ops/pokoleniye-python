from decimal import Decimal as D

s = '12.3 1.8 3.6 -1.2 0.5 -14.2 86.5 10.3'

decimal_lst = [D(num) for num in s.split()]
print(sum(decimal_lst))
print(*sorted(decimal_lst, reverse=True)[:5])