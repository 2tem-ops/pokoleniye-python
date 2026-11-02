import turtle as t

t.speed('fastest')
t.pensize(3)

def diamond(width: int, height: int) -> None:
    t.forward(width)
    t.left(120)
    t.forward(height)
    t.left(60)
    t.forward(width)
    t.left(120)
    t.forward(height)

diamond(100, 100)

t.exitonclick()