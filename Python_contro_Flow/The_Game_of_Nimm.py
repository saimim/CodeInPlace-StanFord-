def main():
    """
    You should write your code here. 
    """
    n = 20  #The game starts with a pile of 20 stones between the players
    p1 = 0
    p2 = 0

    while 1 :
        #play1
        print("There are",n,"stones left.")
        stn = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        while stn>2 or stn<1:
            stn = int(input("Please enter 1 or 2:"))
        n = n-stn
        if n<=0 :
            p2 = 1;
            break;
        print("")
        #play2
        print("There are",n,"stones left.")
        stn = int(input("Player 2 would you like to remove 1 or 2 stones? "))
        while stn>2 or stn<1:
            stn = int(input("Please enter 1 or 2:"))
        n = n-stn
        if n<=0 :
            p1 = 1;
            break;
        print("")
    print(" ")
    if p2 == 1:
        print("Player 2 wins!")
    elif p1 == 1:
        print("Player 1 wins!")        


if __name__ == '__main__':
    main()