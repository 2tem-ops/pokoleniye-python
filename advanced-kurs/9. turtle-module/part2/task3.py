import turtle as t

t.pensize(3)

def quadrant(side: int) -> None:
    t.forward(side)
    t.stamp()
    t.backward(side * 2)
    t.left(180)
    t.stamp()
    t.left(180)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.stamp()
    t.backward(side * 2)
    t.left(180)
    t.stamp()
    t.left(180)
    t.forward(side)

def web(side: int) -> None:
    t.forward(side)
    t.stamp()
    t.backward(side)
    t.dot(side // 10)
    t.backward(side)
    t.left(180)
    t.stamp()
    t.left(180)

    t.forward(side)
    t.left(90)
    t.forward(side)
    t.stamp()
    t.backward(side * 2)
    t.left(180)
    t.stamp()
    t.left(180)
    t.forward(side)

    t.left(45)

    quadrant(side)

web(200)
t.exitonclick()