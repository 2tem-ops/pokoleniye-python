# Only even numbers

counter = 0

for _ in range(1, 11):
    num = int(input())
    if num % 2 == 0:
        counter += 1

if counter == 10:
    print("YES")
else:
    print("NO")