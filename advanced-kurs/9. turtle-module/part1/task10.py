import turtle as t

def star(side: int) -> None:
    t.left(144)
    t.forward(side)
    for _ in range(4):
        t.right(144)
        t.forward(side)

star(200)

t.exitonclick()