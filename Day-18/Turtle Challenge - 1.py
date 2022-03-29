from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for _ in range(4):
    tim.forward(100)
    tim.left(90)

screen.exitonclick()