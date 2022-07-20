import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.goto(100,100)#asi se mueve la tortuga a el punto 100y, 100x y se muestra con una linea inclinada, pero se puede borrar
t.goto(-100, 100)
t.goto(0,0)
t.home()#este comando es para regresar el lapiz a el lugar de inicio

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

turtle.done()