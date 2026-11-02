numbers = [2 + 2j, 3 - 4j, 10 + 6j, -4 + 12j, 12 - 5j]

print(max([i for i in numbers], key=abs), abs(max([i for i in numbers], key=abs)), sep="\n")