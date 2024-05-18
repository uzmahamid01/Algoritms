import turtle
my_turtle = turtle.Turtle()
my_win = turtle.Screen()
def draw_spiral(my_turtle, lineLen):
    if lineLen > 0:
        my_turtle.forward(lineLen)
        my_turtle.right(90)
        draw_spiral(my_turtle, lineLen - 5)

draw_spiral(my_turtle, 100)
my_win.exitonclick()