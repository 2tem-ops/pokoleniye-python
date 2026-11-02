import turtle

def rectangle(width: int, height: int):
    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)
        width, height = height, width

rectangle(100, 200)

turtle.exitonclick()