# Сумма всех

file = open(input(), "r", encoding="utf-8")

print(sum(int(num) for num in file.readlines()))

file.close()