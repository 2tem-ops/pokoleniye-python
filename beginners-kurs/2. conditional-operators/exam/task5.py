num = int(input())

if num % 2 != 0:
    print("YES")
elif num % 2 == 0 and 2 <= num <= 5:
    print("NO")
elif num % 2 == 0 and 6 <= num <= 20:
    print("YES")
elif num % 2 == 0 and num > 20:
    print("NO")