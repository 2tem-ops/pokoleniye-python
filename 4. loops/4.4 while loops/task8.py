# Сколько ждать?

person = input()
counter = 0

while person != "Александра":
    person = input()

person = input()

while person != "Левон":
    counter += 1
    person = input()

print(counter)