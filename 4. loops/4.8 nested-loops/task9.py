# Делители-1

n = int(input())

counter = 0

for i in range(1, n + 1):
    counter = 0
    for k in range(1, i + 1):
        if i % k == 0:
            counter += 1
    print(str(i), "+" * counter, sep="")