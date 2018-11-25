import turtle

def geometricShapes(someTurtle):
    for i in range(1,4):
        someTurtle.forward(100)
        someTurtle.left(120)

##def triangle(otherTurtle):
##    for i in range(1,4):
##        otherTurtle.forward(80)
##        otherTurtle.left(120)

def drawArt():
    window = turtle.Screen()
    window.bgcolor('black')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('white')
    brad.speed(5)
    for i in range(1,37):
        geometricShapes(brad)
        brad.right(10)
    
##    angie = turtle.Turtle()
##    angie.shape('arrow')
##    angie.color('yellow')
##    angie.circle(100)
##
##    mat = turtle.Turtle()
##    mat.shape('square')
##    mat.color('pink')
##    triangle(mat)

    window.exitonclick()


drawArt()


