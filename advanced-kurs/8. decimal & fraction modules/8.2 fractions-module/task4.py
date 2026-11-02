# Операции над дробями

from fractions import Fraction as F

f1_un, f2_un = input(), input()
f1, f2 = F(f1_un), F(f2_un)

print(f"{f1_un} + {f2_un} = {f1 + f2}",
      f"{f1_un} - {f2_un} = {f1 - f2}",
      f"{f1_un} * {f2_un} = {f1 * f2}",
      f"{f1_un} / {f2_un} = {f1 / f2}", sep="\n")