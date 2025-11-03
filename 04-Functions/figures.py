import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

def draw_square(length):
    # Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_trangle(length):
    for i in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(length_a, length_b):
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)

def move_turtle(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def end():
    pen.hideturtle()
    window.mainloop()