# Статистика по файлу

with open(input(), "r", encoding="utf-8") as file:
    lines = [line.split() for line in file.readlines()]
    letters = [char for lst in lines for line in lst for char in line if char.isalpha()]
    print("Input file contains:",
          f"{len(letters)} letters",
          f"{sum(len(line) for line in lines)} words",
          f"{len(lines)} lines", sep="\n")