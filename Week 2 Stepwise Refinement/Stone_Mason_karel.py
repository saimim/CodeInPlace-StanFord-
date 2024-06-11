from stanfordkarel import *

def main():
    phase()
    step()
    phase()
    step()
    phase()
    step()
    phase()



def step():
    for i in range(4):
        move()  

def phase():
    turn_left()
    acc1()
    turn_arround()
    while front_is_clear():
        move()
    turn_left()


def acc1():
    while no_beepers_present():
        put_beeper()
        if front_is_clear():
            move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_arround():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    run_karel_program()