from stanfordkarel import *

def main():
    while front_is_clear():
        move()
    for i in range(8):
        turn_left()
        while right_is_blocked():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program()