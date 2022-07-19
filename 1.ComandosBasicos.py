import turtle

s = turtle.Screen() #asi se creara la pantalla
t = turtle.Turtle()#es el lapiz para dibujar
t.backward(100)#esto crea una linea de 100px para el vector hacia atras
t.write(90)#esto mueve la pluma hacia la derecha
t.forward(100)#hace una linea hacia delante
t.left(90)#esto mueve la linea hacia la izquierda

#se puede abreviar
t.fd(100)#forward
t.rt(90)#write
t.fd(100)#forward
t.lt(90)#left
t.bk(100)#Backward

turtle.done() #esto hace que la pantalla se quede fija (o sea que no se cierre hasta que yo lo ordene)
