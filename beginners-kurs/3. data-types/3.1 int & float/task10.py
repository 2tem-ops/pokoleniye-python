# Интересное число

num = int(input())

first = num // 100
second = num // 10 - first * 10
third = num % 100 - second * 10

if first - third == second or third - first == second or second - first == third or first - second == third or third - second == first or second - third == first:
    print("Число интересное")
else:
    print("Число неинтересное")