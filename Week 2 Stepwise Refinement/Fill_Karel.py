from stanfordkarel import*

def main():
    while front_is_clear():
        acc1()
        turn()


def turn():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
        turn_right()
    else:
        turn_right()
        while front_is_clear():
         move()

def acc1():
    while no_beepers_present():
        put_beeper()
        if front_is_clear():
            move()


def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()