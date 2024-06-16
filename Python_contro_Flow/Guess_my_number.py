import random

n = int(input("Enter a number: "))

dies_num = 5

rnd = random.randint(1,dies_num)

while n!=rnd:
    if rnd<n:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

    print(" ")
    n = int(input("Enter a new guess: "))

print("Congrats! The number was: ",rnd)

