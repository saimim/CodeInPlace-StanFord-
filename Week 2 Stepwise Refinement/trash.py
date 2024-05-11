from stanfordkarel import *

def main():
    while front_is_clear():
        acc()
        put_beeper()
        turn_arround()
        acc()
        turn_right()
        if front_is_clear():
            step_pass()
    turn_right()
    acc()
        

    
    
def step_pass():
    if front_is_clear():
        move()
        turn_right()
def acc():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    

def turn_right():
    for i in range(3):
        turn_left()

def turn_arround():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    run_karel_program()