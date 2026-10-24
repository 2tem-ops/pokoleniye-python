# Переворот числа

n = input()

result = int(n[-5:][::-1]) if len(n) == 5 else n[0] + n[-5:][::-1]

print(result)
