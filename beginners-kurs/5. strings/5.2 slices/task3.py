# Делаем срезы 2

s = input()

third = s[2]
second_last = s[-2]
first_five = s[:5]
except_2 = s[:-2]
even = s[::2]
odd = s[1::2]
backwards = s[::-1]
for_one = s[::-2]

print(
    third, second_last, first_five,
    except_2, even, odd, backwards,
    for_one, sep="\n"
)
