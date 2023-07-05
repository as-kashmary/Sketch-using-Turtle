from turtle import *
tim=Turtle();
screen=Screen();
def move_forward():
    tim.forward(100);

def move_backwards():
    tim.right(180);
    tim.forward(100);
    tim.right(180);

def move_right():
    tim.right(10);

def move_left():
    tim.left(10);

def tim_clear():
    tim.reset();
screen.listen();

screen.onkey(key="w",fun=move_forward)
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=tim_clear, key="space")
screen.exitonclick();
