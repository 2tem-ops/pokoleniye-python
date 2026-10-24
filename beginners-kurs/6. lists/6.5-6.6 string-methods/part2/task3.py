# Взлом Братства Стали

s = input()
n = int(s[1:])

for _ in range(n):
    code = input()
    hashtag = code.find("#")

    if hashtag != -1:
        code = code[:hashtag].rstrip()

    print(code.rstrip())