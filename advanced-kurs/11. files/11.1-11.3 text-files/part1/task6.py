# Общая стоимость

file = open(input(), "r", encoding="utf-8")

total = 0

for line in file.read().split("\n"):
    product, amount, price = line.replace("\t", " ").split()
    total += int(amount) * int(price)

print(total)

file.close()