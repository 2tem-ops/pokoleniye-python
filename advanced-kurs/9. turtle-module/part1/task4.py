import turtle as t

t.speed('fastest')

def square(side: int) -> None:
    for _ in range(4):
        t.forward(side)
        t.left(90)

def do() -> None:
    square(200)
    t.back(200)
    square(200)
    t.right(90)
    square(200)
    t.left(90)
    t.forward(200)
    t.right(90)
    square(200)

for _ in range(2):
    do()
    t.left(50)

t.exitonclick()