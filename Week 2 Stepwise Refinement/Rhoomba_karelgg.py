from stanfordkarel import *


'''
1. at first acc(east) er maddhome karel ke running korte hobe
2. dekhte hobe always east face korteche kina  er sathe dekhte hobe front clear kina karon east face korleo front clear nao hote pare sekhettre code crash korbe
3. erpor satate ment er kaj korte hobe
4. ekhane portek while condition er moddhe break use kora hoice jeno karel infinity loop er moddhe pore na jai ar turn er jonno use kora hoice last phase piye gele jeno code theke jai.
'''

def main():
    while front_is_clear():
        acc()
        turn1()
        acc_west()
        turn2()

def clear_beeper():
    if beepers_present():
        pick_beeper()

def acc():
    while facing_east():
        while front_is_clear():
            clear_beeper()
            move()
        break
    clear_beeper()

def acc_west():
    while facing_west():
        while front_is_clear():
            clear_beeper()
            move()
        break
    clear_beeper()

def turn1():
    while left_is_clear():
        step_up()
        break
    turn_left()

def turn2():
    while right_is_clear():
        turn_right()
        move()
        break
    turn_right()

def step_up():
    turn_left()
    move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program()