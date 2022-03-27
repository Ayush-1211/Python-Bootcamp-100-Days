from turtle import Turtle, Screen

timmy = Turtle()        # Object: timmy, Class: Turtle
print(timmy)

timmy.shape("turtle")       # Object: timmy, Method: shape
timmy.color("black")
timmy.forward(100)

my_screen = Screen()    # Class: Screen
print(my_screen.canvwidth)  # Object: my_screen, Attribute: canvwidth
my_screen.exitonclick()     # Method: exitonclick