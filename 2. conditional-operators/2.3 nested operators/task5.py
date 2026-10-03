# Церемония взвешивания

weight = int(input())

if weight < 60:
    print("Легкий вес")
elif weight < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")