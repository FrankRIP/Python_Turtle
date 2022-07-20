import turtle
import random

s= turtle.Screen()
s.title("Primer Proyecto")
s.bgcolor("gray")

t1= turtle.Turtle()
t2= turtle.Turtle()

t1.hideturtle()
t1.shape("turtle")
t1.color("blue", "blue")
t1.shapesize(2,2,2)
t1.pensize(3)


t2.hideturtle()
t2.shape("turtle")
t2.color("red", "red")
t2.shapesize(2,2,2)
t2.pensize(3)


t1.penup()
t1.goto(200, 200)
t1.pendown()
t1.circle(40)
t1.penup()
t1.goto(-250, 225)
t1.showturtle()

t2.penup()
t2.goto(200, -200)
t2.pendown()
t2.circle(40)
t2.penup()
t2.goto(-250, -170)
t2.showturtle()

dado = [1, 2, 3, 4, 5, 6]

for i in range (20):
    if t1.pos() >=0 (200, 200):
        print("La tortuga azul ha ganado")
        break
    elif t2.pos() >= (200, -200):
        print("La tortuga roja ha ganado")
        break
    else:
        turno1 = input("Presiona Enter para continuar")
        turno1 = random.choice(dado)
        print("Tu numero en dado es: ",turno1,"\nAvanzas: ",turno1*20)
        t1.pendown()
        t1.forward(20*turno1)

        turno2 = input("Presiona Enter para continuar")
        turno2 = random.choice(dado)
        print("Tu numero en dado es: ",turno2,"\nAvanzas: ",turno2*20)
        t2.pendown()
        t2.forward(20*turno2)

turtle.done()