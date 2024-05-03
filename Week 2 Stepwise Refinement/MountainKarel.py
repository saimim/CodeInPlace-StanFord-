from stanfordkarel import *

def main():
 climb_mountain()
 put_beeper()
 climb_down()

def climb_mountain():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()
def turn_right():
    for i in range(3):
        turn_left()
def climb_down():
   while front_is_clear():
      move()
      turn_right()
      move()
      turn_left()

if __name__== '__main__':
   run_karel_program()
