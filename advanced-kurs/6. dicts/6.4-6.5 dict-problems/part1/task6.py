# Телефонная книга

phonebook = {}

for _ in range(int(input())):
    person = input().split()
    phonebook.setdefault(person[1], []).append(person[0])

for _ in range(int(input())):
    print(*phonebook.get(input().capitalize(), ["абонент не найден"]))