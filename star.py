import turtle

a = turtle.Turtle()
turtle.bgcolor("black")
a.speed(0)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']


def star(n):
    for i in range(5):
        a.fd(n)
        a.rt(144)


j = 50
for i in range(50):
    a.color(colors[i % 7])
    star(j)
    a.rt(10)
    j += 10

pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
turtle.done()
