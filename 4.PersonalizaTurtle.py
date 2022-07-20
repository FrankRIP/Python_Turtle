import turtle

s= turtle.Screen()
t= turtle.Turtle()

s.bgcolor("Gray")#para cambiar el color de lienzo
s.title("Proyecto Juanito")#se cambia el nombre al lienzo

t.shapesize(10, 5, 1)#(largo, ancho y borde) es para cambiarle el tamaño a la tortuga
t.shapesize(3, 3, 3)

t.fillcolor("White")#fillcolor es para cambiarle el colo de relleno de la tortuga
t.forward(40)

t.pencolor("blue")#cambia el color del borde
t.forward(100)

t.color("green", "blue")#cambio el color de la tinta y luego el de la tortuga
t.right(90)
t.forward(100)

t.pensize(5)#es para cambiar el tamaño del trazo de la tinta
t.forward(200)

turtle.done()