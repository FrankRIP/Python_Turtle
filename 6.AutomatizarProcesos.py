import turtle

s= turtle.Screen()
t= turtle.Turtle()
i = 0

'''
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
'''
resultado= input("¿Quieres imprimir una figura?")

for i in range (4):
    t.forward(100)
    t.right(90)

if resultado== "si":
    while i <=100:
        t.circle(i)
        i += 10
else: 
    print("Oka")

turtle.done()