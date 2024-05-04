from stanfordkarel import *

def main():
    while left_is_clear():
        clear_row()
        reset_to_next_row()
    clear_row()

def clear_row():
     while front_is_clear():
          clear_corner()
          move()
     clear_corner()

def clear_corner():
     if beepers_present():
          pick_beeper()

def reset_to_next_row():
     turn_arround()
     move_to_wall()
     turn_right()
     move()
     turn_right()

def move_to_wall():
     while front_is_clear():
          move()

def turn_arround():
     turn_left()
     turn_left()          

def turn_right():
     for i in range(3):
          turn_left()

if __name__ == '__main__':
     run_karel_program()
