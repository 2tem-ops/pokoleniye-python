from turtle import *

tracer(0)
m = 35
screensize(10000, 10000)

for _ in range(2):
    fd(3 * m); rt(90); fd(20 * m); rt(90)

up()

bk(8 * m); rt(90); fd(9 * m); lt(90)

down()

for _ in range(2):
    fd(16 * m); rt(90); fd(8 * m); rt(90)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
exitonclick()