from turtle import *

tracer(0)
screensize(10000, 10000)
m = 35

for _ in range(2):
    fd(11 * m); rt(90); fd(17 * m); rt(90)

up()

fd(7 * m); lt(90); bk(1 * m); rt(90)

down()

for _ in range(2):
    fd(15 * m); rt(90); fd(7 * m); rt(90)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
exitonclick()