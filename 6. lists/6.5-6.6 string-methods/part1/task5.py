# Корректный ip-адрес

s = input()
ip = s.split(".")
flag = True

for num in ip:
    if int(num) > 255:
        flag = False

if flag:
    print("ДА")
else:
    print("НЕТ")