from random import sample

def generate_bingo() -> list[list[int]]:
    numbers = sample([*range(1, 76)], 25)

    bingo = [[int(str(numbers.pop()).ljust(3)) for _ in range(5)] for _ in range(5)]
    bingo[2][2] = 0
    return bingo

print(generate_bingo())