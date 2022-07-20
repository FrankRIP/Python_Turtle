import turtle

s= turtle.Screen()
t= turtle.Turtle()
'''
t.begin_fill()#inicia el relleno
t.circle(100)
t.end_fill()#termina el relleno

t.begin_fill()
t.color("white", "white")
t.circle(50)
t.end_fill()
'''

t.shape("turtle")

t.forward(100)
t.penup()#levanta el lapicero
t.forward(100)
t.pendown()#baja el lapicero
t.forward(100)

t.undo()#es para deshacer la ultima accion
t.clear()#para limpiar toda la pantalla
t.reset()#se reinicia todo el programa

t.forward(100)
t.stamp()#es para dejar una marca de agua
t.forward(100)

turtle.done()