from random import choice

class MagicBall:
    def __init__(self):
        self.__answers: list[str] = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом",
                                     "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
                                     "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять",
                                     "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

    def answer(self) -> str:
        return choice(self.__answers)

class MagicBallGame:
    def __init__(self):
        self.__ball = MagicBall()

    def __introduction(self):
        print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
        name = input("Введите имя: ")
        print(f"Привет {name}!", end="\n\n")

    def __question(self):
        input("Задай вопрос, на который можно ответить да или нет: ")
        print(self.__ball.answer())
        print("")

    def exec(self):
        self.__introduction()
        while True:
            self.__question()
            repeat = input("Хотите задать ещё вопрос? ('д'/'н'): ")
            if repeat.lower() == "д":
                print("")
                self.__question()
            if repeat.lower() == "н":
                print("Возвращайся, если возникнут вопросы!")
                break
            else:
                print("Неправильный ввод")
                break

def main():
    game = MagicBallGame()
    game.exec()

if __name__ == "__main__":
    main()