import turtle
import random as rd

sides = 3
angle = 60
sideLength = 500
vertices = []
direction = 0
turtle.getscreen().tracer(0, 0)
turtle.screensize(1920, 1080)

#draw initial shape
for i in range(sides):
    turtle.forward(sideLength)
    turtle.right(180+angle)
    vertices.append(turtle.pos()) 

turtle.penup()

#rough attempt to pick a random point that should be inside any potential
#shape if we alter sides/angle searching for patterns in other shapes
turtle.setpos(rd.randrange(vertices[0][0]//4,(vertices[0][0]//4)*3),rd.randrange(vertices[sides//2][1]//2))  

#pick random points and draw a dot
for i in range(50000):
    direction = vertices[rd.randint(0,sides-1)]
    turtle.setheading(turtle.towards(direction))
    turtle.forward(turtle.distance(direction)/2)
    turtle.dot(2,"black")

turtle.done()