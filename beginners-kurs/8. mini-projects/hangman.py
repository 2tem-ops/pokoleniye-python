from wonderwords import RandomWord
from faker import Faker

class Hangman:
    def __init__(self):
        self.word = Faker('ru_RU').word().upper()
        self.word_completion = ("_ " * len(self.word)).split()
        self.tries = 6
        self.__stages = [
            r'''
┌───┐
│   │
│   ○
│  /|\
│  / \
┴───────
            ''',
            r'''
┌───┐
│   │
│   ○
│  /|\
│  / 
┴───────
            ''',
            r'''
┌───┐
│   │
│   ○
│  /|\
│
┴───────
            ''',
            r'''
┌───┐
│   │
│   ○
│  /|
│
┴───────
            ''',
            r'''
┌───┐
│   │
│   ○
│   |
│
┴───────
            ''',
            r'''
┌───┐
│   │
│   ○
│
│
┴───────
            ''',
            r'''
┌───┐
│   │
│
│
│
┴───────
            ''',
        ]

    def fail_try(self):
        self.tries -= 1

    def guess_letter(self, guess: str):
        if guess in self.word:
            indices = [int(index) for index, letter in enumerate(self.word) if letter == guess]
            for index in indices:
                self.word_completion[index] = guess
            return True
        return False

    def get_stage(self):
        return self.__stages[self.tries]

class Game:
    def __init__(self):
        self.__hangman = Hangman()
        self.__word = self.__hangman.word

    def __attempt(self):
        print(self.__hangman.get_stage())
        print("".join(self.__hangman.word_completion))

        guess = input("Введи букву: ").upper()

        if not guess.isalpha():
            print("Нужно ввести букву!")
            self.__attempt()

        if not self.__hangman.guess_letter(guess):
            self.__hangman.fail_try()

    def __active(self) -> bool:
        if "".join(self.__hangman.word_completion).isalpha():
            return False
        if self.__hangman.tries <= 0:
            return False

        return True

    def exec(self):
        print("---------- Сыграем в угадайку слов! ----------")

        while self.__active():
            self.__attempt()

        if self.__hangman.tries <= 0:
            print(self.__hangman.get_stage())
            print("Ты проиграл :(")
            print(f"Слово: {self.__word}")

        if "".join(self.__hangman.word_completion) == self.__word:
            print("")
            print(f"{self.__word}", "Ура! Ты угадал :)", sep="\n")

def main():
    hangman = Game()
    hangman.exec()

if __name__ == "__main__":
    main()