import turtle

def triangle(side: int) -> None:
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)

triangle(200)

turtle.exitonclick()