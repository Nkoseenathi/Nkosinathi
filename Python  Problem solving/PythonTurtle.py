import turtle
# Create multiple turtles
a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()
e=turtle.Turtle()
f=turtle.Turtle()

# Draw the body of the turtle
a.color("black", "red")
a.circle(100,360)
a.end_fill()

# Draw the heard of the turtle
a.ht()
b.up()
b.goto(-100,100)
b.down()

for i in range(3):
    b.forward(25)
    b.right(90)

b.right(-90)
b.forward(5)
b.ht()

# Draw the first leg of the turtle
c.up()
c.goto(-150,78)
c.down()
c.right(-30)

for i in range(3):

    if i==1:
        c.forward(25)
    else:
        c.forward(55)
    
    c.right(-90)
    
c.right(90)
c.forward(12)
c.ht()

# Draw the second leg of the turtle
d.up()
d.goto(-37,70)
d.down()
d.right(30)

for i in range(3):
    if i==1:
        d.forward(25)
    else:
        d.forward(60)
    
    d.left(-90)
    
d.right(-90)
d.forward(12)
d.ht()

# Draw the third leg of the turtle
e.up()
e.goto(-37,-70)
e.down()
e.right(-30)

for i in range(3):
    if i==1:
        e.forward(-25)
    else:
        e.forward(-60)
    
    e.left(-90)
    
e.right(-90)
e.ht()

# Draw the last leg of the turtle
f.up()
f.goto(-150,-88)
f.down()
f.right(30)

for i in range(3):
    if i==1:
        f.forward(-25)
    else:
        f.forward(-55)
    
    f.right(90)
    
f.right(-90)
f.forward(-17)
f.ht()

turtle.exitonclick()
