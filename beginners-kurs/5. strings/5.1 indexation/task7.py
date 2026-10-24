# Сколько раз?

s = input()

plus = ""
star = ""

for c in s:
    if c == "*":
        star += c
    elif c == "+":
        plus += c

print(f"Символ + встречается {len(plus)} раз",
      f"Символ * встречается {len(star)} раз",
      sep="\n"
)
