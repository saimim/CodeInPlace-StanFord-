import random 

num_sides = 6

print("Total",num_sides,"sides")
die1 = random.randint(1,num_sides)
die2 = random.uniform(1,num_sides)
print("First die:",die1)
print("Second die:",die2)
print("Total:",die1+die2)

