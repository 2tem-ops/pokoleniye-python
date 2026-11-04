# Сумма двух

file = open(input(), 'r', encoding='utf-8')
a, b = file.readlines()
print(int(a) + int(b))
file.close()