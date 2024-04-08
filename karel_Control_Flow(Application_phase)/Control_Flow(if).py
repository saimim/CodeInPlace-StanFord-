from stanfordkarel import *

def main():
    while 1:
      for i in range(2):
         acc2()
      acc1()
      for i in range(2):
         acc2()
      acc1()

def acc1():
  turn_left()
  invert_beepers()
  move()
  turn_left()   

def acc2():
     invert_beepers()
     move()

def invert_beepers():
        if beepers_present():
            pick_beeper()
        else:
            put_beeper()
if __name__ == '__main__':
    run_karel_program()