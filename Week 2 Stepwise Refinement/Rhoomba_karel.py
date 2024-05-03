from stanfordkarel import *

def main():
    while front_is_clear:
        clear_front()
        front_is_blocked()                      
        move()                                     
        turn_left()
        clear_front()
        turn_right()

def clear_front():
    while front_is_clear():
            while beepers_present():
                 pick_beeper()
                 move()
            while no_beepers_present():
                 move()

def turn_right():
     for i in range(3):
          turn_left()

def front_is_block():
     while front_is_blocked():
         while facing_east():
              turn_left()
         while facing_west():                 
              turn_right()

if __name__ == '__main__':
     run_karel_program()