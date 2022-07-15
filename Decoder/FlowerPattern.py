import turtle
t=turtle.Turtle()

# Get the number of  petals from the user
petals=int(turtle.numinput('Number of petals','Enter the number of petals (must be an even number): '))

# Get the size of the stem from the user
stem_length=int(turtle.numinput('Stem length','Enter the length of stem: '))

# Get the petal type from the user
petal_type=(turtle.textinput('Petal type','Enter the petal type (triangle, square, or pentagon): '))

# Get the length of  side from the user
length_of_side=int(turtle.numinput('length of side','Enter the length of side: '))

# Get the stem colour from the user
stem_color=turtle.textinput('Stem colour','Enter the stem colour: ')

# Get the first petal colour from the user
first_petal_color=turtle.textinput('First petal color','Enter the first petal colour: ')

# Get the second  petal colour from the user
second_petal_color=turtle.textinput('Second petal colour','Enter the second petal colour: ')

# create a method with 4 arguments
def main(interior_angle,sides,tri,pent):

    # set the angle between the the petals to 360/petals
    angles=360/petals

    for i in range(1,petals+1):

        # put the pen down
        t.down()

        # Change the pen color to the color obtained from the user
        t.color(stem_color)

        # Move the turtle by the amount of steps obtained from the user
        t.forward(stem_length)

        if pent!=0:
            # if the argument pent does not equals to zero turn the turtle pent degrees to the left
            t.left(pent)

        else:
            # if the argument pent equals to zero turn the turtle half of interior_angle degrees to the left
            t.left(interior_angle*0.5*tri)  
      
        if i%2==0:
            # If the controling variable modulus 2 is 0 change the color to the second petal colour obtained from the user
            t.color(second_petal_color)

        else:
            # If the controling variable modulus 2 is not 0 change the color to the first petal colour obtained from the user
            t.color(first_petal_color)        
        
        # Draw a petal
        for i in range(sides):
            t.forward(stem_length)
            t.right(interior_angle)

        # pick the pen up
        t.up()

        # Move the turtle to its default position
        t.home()

        # turn turtle the variable angle degrees to the right
        t.right(angles)

        # Increment the angle between the petals by 360/number of petals
        angles+=360/petals
        

if petal_type=='triangle': 
    # if petal type is triangle call the main method and put in proper arguments
    main(120,3,0.5,0)

if petal_type=='square': 
    # if petal type is square call the main method and put in proper arguments
    main(90,4,1,0)

if petal_type=='pentagon':  
    # if petal type is pentagon call the main method and put in proper arguments
    main(72,5,1,54)
    

# Close the turtle dialogue
turtle.exitonclick()