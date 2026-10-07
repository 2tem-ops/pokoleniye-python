# Второе вхождение

text = input()

if text.count("f") > 1:
    start = text.find("f") + 1
    part_1 = len(text[:start])
    f = text.find("f", part_1)
    print(f)
elif text.count("f") == 1:
    print(-1)
else:
    print(-2)