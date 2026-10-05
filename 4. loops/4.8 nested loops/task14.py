# Делители-2

a, b = int(input()), int(input()) # a < b
comb = 0
largest = 0

for i in range(a, b + 1):
    comb = 0
    for k in range(1, i + 1):
        if i % k == 0:
            comb += k
            if comb >= largest:
                largest = comb
                latest = i

print(latest, largest)
