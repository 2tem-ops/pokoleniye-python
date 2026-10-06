# Первое и последнее вхождение

text = input()

if text.count("f") == 1:
    print(text.find("f"))
elif text.count("f") >= 2:
    print(text.find("f"), text.rfind("f"))
else:
    print("NO")