# Цифровой корень

n = int(input())
dig = len(str(n))

total = 0
total2 = 0


for i in range(dig + 1):
    total += (n // 10 ** i) % 10

dig2 = len(str(total))

while len(str(total)) > 1:
    new_total = 0

    for j in range(len(str(total))):
        new_total += (total // 10 ** j) % 10
    total = new_total

print(total)