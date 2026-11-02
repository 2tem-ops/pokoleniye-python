from fractions import Fraction as F

numbers = ['3.1415', '-2.8', '4.123', '7.856']

for num in numbers: print(f"{num} = {F(num)}")