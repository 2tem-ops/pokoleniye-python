from turtle import *

screensize(10000, 10000)
m = 40
tracer(0)

for _ in range(2):
    fd(13 * m); rt(90); fd(18 * m); rt(90)

up()

fd(5 * m); rt(90); fd(9 * m); lt(90)

down()

for _ in range(2):
    fd(11 * m); rt(90); fd(7 * m); rt(90)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
exitonclick()