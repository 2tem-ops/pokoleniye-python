# Упорядоченные дроби

from fractions import Fraction as F

fracs = set()

for i in range(1, int(input()) + 1):
    for j in range(1, i):
        fracs.add(F(j, i))

print(*sorted(fracs), sep="\n")