# Третья цифра

n = int(input())
length = len(str(n))
opp = n // (10 ** (length - 3))
print(opp % 10)


