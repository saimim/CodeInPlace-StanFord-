from stanfordkarel import *

def main():
    """ for i in range(4):
        put_beeper()
        move()
        turn_left()
    for i in range(4):
        pick_beeper()
        move()
        turn_left() """
    
    for i in range(2):
        put_beeper()
        move()
    acc()
    for i in range(2):
     put_beeper()
     move()
    acc()
    
def acc():
   put_beeper()
   turn_left()
   move()
   turn_left()

if __name__=='__main__':
    run_karel_program()