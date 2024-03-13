import turtle

tur = turtle.Turtle()
tur.speed(1) 
tur.getscreen().bgcolor("black")
tur.color("cyan")
tur.penup() 
tur.goto((-200, 0))
tur.pendown()
  
sides = 5
angle = 144
scalar = 2.5
size = 400

def fractal(turtle, size):
    '''Basic recursive function to draw fractal patterns using regular shapes'''
    if size <= 10:
        return
    else:
        for i in range(sides):
            turtle.forward(size)
            fractal(turtle, size/scalar)
            turtle.left(angle)

fractal(tur, size)
