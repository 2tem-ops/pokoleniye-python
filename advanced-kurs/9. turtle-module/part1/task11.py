import turtle as t

def step() -> None:
    t.setheading(90)
    for i in range(1, 20, 5):
        t.forward(i * 20)
        t.left(90)
step()
t.exitonclick()