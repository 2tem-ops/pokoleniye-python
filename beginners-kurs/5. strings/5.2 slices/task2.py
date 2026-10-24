# Делаем срезы 1

s = input()

symbols = len(s)
three_times = s * 3
first = s[0]
first_three = s[0:3]
last_three = s[-3:]
backwards = s[::-1]
no_end_or_start = s[1:-1]

print(
    symbols, three_times, first,
    first_three, last_three, backwards,
    no_end_or_start,
    sep="\n"
)