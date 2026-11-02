import turtle as t

t.speed('fastest')
t.pensize(3)

def hexagon(side: int) -> None:
    for _ in range(6):
        t.forward(side)
        t.left(60)

hexagon(200)

t.exitonclick()