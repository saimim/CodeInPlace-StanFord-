import random

num_sides = 6

#Simulates rolling two dice and prints their total

def roll_dice():
    die1 = random.randint(1,num_sides)
    die2 = random.randint(1,num_sides)
    total = die1+die2
    print("Total of two dice:",total)

def main():
    die1 = 10
    print("die1 in main() starts as:",die1)
    roll_dice()
    roll_dice()
   # roll_dice()
    print("die1 in main() is:",die1)

if __name__=="__main__":
    main()