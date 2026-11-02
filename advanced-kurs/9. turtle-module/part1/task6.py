import turtle as t

t.speed('fastest')
t.pensize(3)

def hexagon(side: int) -> None:
    for _ in range(6):
        t.left(60)
        for _ in range(5):
            t.forward(side)
            t.left(60)
        t.left(60)
    for _ in range(6):
        t.right(60)
        t.forward(side)

hexagon(100)

t.exitonclick()