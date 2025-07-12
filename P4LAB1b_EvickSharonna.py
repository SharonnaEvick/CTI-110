# p4LAB1b_EvickSharonna.py
import turtle

# Set up turtle
t = turtle.Turtle()
t.pensize(8)
t.color("purple")
t.speed(2)

# Draw the letter S using a loop (top arc and bottom arc)
t.penup()
t.goto(-150, 0)
t.setheading(0)
t.pendown()

# Top half curve of S (turn left in small steps)
for _ in range(30):
    t.forward(4)
    t.left(5)

# Bottom half curve of S (turn right in small steps)
for _ in range(30):
    t.forward(4)
    t.right(5)


# Move to position for E
t.penup()
t.goto(50, 0)
t.setheading(0)
t.pendown()

# Draw the letter E (without a loop, but that’s fine since we used one above)
t.forward(50)
t.backward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.backward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)

# Finish drawing
turtle.done()
