from stanfordkarel import *

def main():
    turn_left()
    while front_is_clear():
        put_beeper()
        while front_is_clear():
            acc2()
        turn_right()    
        if front_is_clear():
            move()
            turn_right()
        while front_is_clear():
            move()
        if facing_south():
            turn_arround()
        if front_is_clear():
            move()
            put_beeper()
        while front_is_clear():
            acc3()
        if facing_north():
            if right_is_clear():
                turn_right()
                move()
                turn_right()
                while front_is_clear():
                    move()
                turn_arround()
    #return home
    if facing_east():
        turn_right()
        while front_is_clear():
            move()
        turn_right()
        while front_is_clear():
            move()
        turn_arround()
    #for 6x6
    if facing_north():
        turn_right()
        if facing_east():
            turn_right()
            while front_is_clear():
                move()
            turn_right()
            while front_is_clear():
                move()
            turn_arround()



def turn_right():
    for i in range(3):
        turn_left()

def turn_arround():
    for i in range(2):
        turn_left()

def acc3():
    move()
    if front_is_clear():
        move()
        put_beeper()


def acc2():
    move()
    if front_is_clear():
        move()
        put_beeper()

if __name__ == "__main__":
    run_karel_program()