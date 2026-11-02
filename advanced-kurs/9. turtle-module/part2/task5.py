import turtle as t

t.shape('turtle')
t.stamp()
t.penup()

def turtle_circle(amount: int, distance: int) -> None:
    angle = 360 / amount

    for _ in range(amount):
        t.forward(distance - 50)
        t.pendown()
        t.forward(30)
        t.penup()
        t.forward(20)
        t.stamp()
        t.backward(distance)
        t.left(angle)

turtle_circle(10, 100)

t.exitonclick()