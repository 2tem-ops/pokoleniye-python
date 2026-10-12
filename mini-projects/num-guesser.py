import random

secret = random.randint(1, 10)
lives = 3

while True:
    try:
        if lives == 0:
            print(f"Ran out of lives. The number was {secret}")
            break

        guess = int(input("Enter a number 1-10: "))
        if guess < 1 or guess > 10:
            print("Number must be between 1-10")
            continue
    except ValueError:
        print("Enter an integer value, not a string!")
        continue

    if guess < secret:
        msg = "Too low! -1 life"
        print(f"{msg:-^24}")
        lives -= 1
        continue
    elif guess > secret:
        msg = "Too high! -1 life"
        print(f"{msg:-^24}")
        lives -= 1
        continue
    else:
        print(f"You guessed the number with {lives} remaining!")
        break