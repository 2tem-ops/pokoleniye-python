# Три города

city1, city2, city3 = input(), input(), input()

smallest = ""
largest = ""

if len(city1) > len(city2) > len(city3):
    smallest = city3
    largest = city1
elif len(city2) > len(city1) > len(city3):
    smallest = city3
    largest = city2
elif len(city3) > len(city1) > len(city2):
    smallest = city2
    largest = city3
elif len(city2) > len(city3) > len(city1):
    smallest = city1
    largest = city2
elif len(city1) > len(city3) > len(city2):
    smallest = city2
    largest = city1
elif len(city3) > len(city2) > len(city1):
    smallest = city1
    largest = city3

print(smallest, largest, sep="\n")


