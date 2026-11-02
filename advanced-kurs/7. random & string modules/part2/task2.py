from random import sample, randint
from string import ascii_uppercase

def generate_index() -> str:
    return f"{"".join(sample(ascii_uppercase, 2))}{randint(0, 99)}_{randint(0, 99)}{"".join(sample(ascii_uppercase, 2))}"

print(generate_index())