import turtle as t

t.shape('turtle')
t.stamp()
t.penup()

def turtle_circle(amount: int, distance: int) -> None:
    angle = 360 / amount

    for _ in range(amount):
        t.forward(distance)
        t.stamp()
        t.backward(distance)
        t.left(angle)

turtle_circle(int(input()), int(input()))

t.exitonclick()