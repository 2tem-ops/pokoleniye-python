import turtle as t

def quadrant(side: int) -> None:
    t.forward(side)
    t.backward(side * 2)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.backward(side * 2)
    t.forward(side)

for _ in range(2):
    quadrant(200)
    t.left(45)

t.exitonclick()