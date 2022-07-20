import turtle

s= turtle.Screen()
t= turtle.Turtle()

t.speed(10)#speed es para aumentar la velocidad de dibujo
t.circle(10)#circle es para crear un circulo
t.speed(10)
t.circle(50)
t.dot(30)#es para ponerle tamaño al diametro del circulo

t.hideturtle()#hideturtle es para que se desaparezca la tortuga
t.speed(1)
t.circle(40)
t.showturtle()#showturtle es para que aparezca la tortuga
t.circle(100)

t.setx(100)#setx hace que se mueva al eje x sin salir del eje y
t.sety(-100)#sety hace que se mueva al eje y sin salir del eje x

turtle.done()