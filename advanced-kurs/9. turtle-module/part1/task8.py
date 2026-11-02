import turtle as t

t.speed('fastest')
t.pensize(3)

def diamond(side: int) -> None:
    t.left(45)
    for _ in range(10):
        t.left(40)
        for _ in range(4):
            t.forward(side)
            t.left(120)
            t.forward(side)
            t.left(60)

diamond(200)

t.exitonclick()