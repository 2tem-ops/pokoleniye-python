# Negatives, Zeros and Positives

n = int(input())

pos, neg, zero = [], [], []

for i in range(n):
    num = int(input())
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero.append(num)

print(*neg, *zero, *pos, sep="\n")

