# max и min

n = int(input())
largest = 0
smallest = 10000

while n > 0:
    last_digit = n % 10
    if last_digit > largest:
        largest = last_digit
    if last_digit < smallest:
        smallest = last_digit
    n //= 10

print(
    f"Максимальная цифра равна {largest}",
    f"Минимальная цифра равна {smallest}",
    sep="\n"
)