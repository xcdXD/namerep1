from turtle import *

screensize(5000,5000)
tracer(0)
m = 20
lt(90)

for _ in range(5):
    fd(29 * m)
    rt(90)
    fd(27 * m)
    rt(90)

up()

fd(3 * m)
rt(90)
fd(9 * m)
lt(90)

down()

for _ in range(5):
    fd(72 * m)
    rt(90)
    fd(95 * m)
    rt(90)

up()

for x in range(-50,50):
    for y in range(-50,50):
        goto(x * m, y * m)
        dot(3,"blue")

update()
mainloop()
