from stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

if __name__ == '__main__':
    run_karel_program()