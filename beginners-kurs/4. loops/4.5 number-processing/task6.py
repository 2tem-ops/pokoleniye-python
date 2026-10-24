# Одинаковые цифры

num = int(input())
n = len(str(num))
digit = ""


while num > 0:
    last_digit = num % 10
    digit += str(last_digit)
    if len(digit) == n:
        break

if int(digit) == num:
    print("YES")
else:
    print("NO")
