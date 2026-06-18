#region шаблон
from turtle import *

screensize(5000,5000)
tracer(0)
m = 20 # m => масштаб
lt(90)
#endregion

#region переписывание условия...

#endregion

#region после условия
"""
всегда в конце условия пишем up()(что бы не забагавалось)

"""

up()

#далее пишем:
for x in range(-30,30): #отвечают за кол-во точек(если точек мало,увелич размер(например => (-50,50))
    for y in range(-30,30):
        goto(x * m, y * m)
        dot(3,"blue")

update()
mainloop()

