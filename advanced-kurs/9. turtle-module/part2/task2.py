import turtle as t

t.pensize(2)

def rectangle(width: int, height: int) -> None:
    for _ in range(4):
        t.forward(width)
        t.dot((width + height) // 10)
        t.left(90)
        width, height = height, width

rectangle(100, 150)
t.exitonclick()