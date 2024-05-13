from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    turn_left()
    while front_is_clear():
        acc()
        if front_is_clear():
            turn_left()
    turn_right()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    put_beeper()
            


def acc():
    if front_is_clear():
         move()
    if front_is_clear():
        move()
        turn_right()
        move()
    

def turn_right():
    for i in range(3):
        turn_left()

def turn_arround():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()