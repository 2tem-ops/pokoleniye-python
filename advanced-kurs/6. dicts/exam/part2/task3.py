# Scrabble game

scrabble = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

s = input()
total = 0

for k, v in scrabble.items():
    v = list(v)
    for char in s:
        if char in v:
            total += k

print(total)