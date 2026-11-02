import turtle as t

t.speed('fastest')

def square(side: int) -> None:
    t.begin_fill()

    for _ in range(6):
        t.left(20)
        for _ in range(4):
            t.forward(side)
            t.left(90)

    t.end_fill()

for _ in range(3):
    square(200)

t.exitonclick()