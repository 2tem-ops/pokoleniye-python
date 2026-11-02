# max + min

from decimal import Decimal as d

num = d(input())

num_stats = num.as_tuple()

if abs(num) > 1:
    print(max(num_stats[1]) + min(num_stats[1]))
else:
    print(max(num_stats[1]))