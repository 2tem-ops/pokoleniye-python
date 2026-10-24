# Координатные четверти

def quadrants(coords: list[tuple[int, int]]):
    first, second, third, fourth = 0, 0, 0, 0

    for coord in coords:
        if coord[0] > 0 and coord[1] > 0:
            first += 1
        elif coord[0] < 0 and coord[1] > 0:
            second += 1
        elif coord[0] < 0 and coord[1] < 0:
            third += 1
        elif coord[0] > 0 and coord[1] < 0:
            fourth += 1
        else:
            pass

    return first, second, third, fourth

amount = int(input())
every = []

for _ in range(amount):
    every.append(tuple([int(i) for i in input().split()]))

first, second, third, fourth = quadrants(every)

print(f"Первая четверть: {first}",
      f"Вторая четверть: {second}",
      f"Третья четверть: {third}",
      f"Четвертая четверть: {fourth}", sep="\n")