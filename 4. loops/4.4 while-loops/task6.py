# Количество пятёрок

num = int(input())
counter = 0

while 5 >= num > 0:
    if num == 5:
        counter += 1
    num = int(input())

print(counter)
