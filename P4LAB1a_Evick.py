# p4LAB1a_Evick.py
import turtle

# Set up turtle
t = turtle.Turtle()
t.pensize(3)
t.color("pink")

# Draw a square using a for loop
for _ in range(4):
    t.forward(100)
    t.right(90)

# Move to a different location for the triangle
t.penup()
t.goto(-150, -150)
t.pendown()
t.color("purple")

# Draw a triangle using a while loop
sides = 0
while sides < 3:
    t.forward(100)
    t.left(120)
    sides += 1

# Finish
turtle.done()
