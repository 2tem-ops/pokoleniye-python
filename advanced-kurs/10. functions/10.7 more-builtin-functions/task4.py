# Корректный IP-адрес


print(all(x.isdigit() and  0 <= int(x) <= 255 for x in input().split(".")))