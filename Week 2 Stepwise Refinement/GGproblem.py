from stanfordkarel import *

def main():
    while front_is_clear():
        acc()
        if front_is_clear():
            move()
    

def acc():
    put_beeper()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    turn_left()
    


def turn_right():
    for i in range(3):
        turn_left()
