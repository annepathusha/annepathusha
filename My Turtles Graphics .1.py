import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colors in ("red","magenta","blue","green","yellow","white","cyan"):
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()