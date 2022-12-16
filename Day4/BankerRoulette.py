import random

names_string = input("Tell me who is at the table: ")
names = names_string.split(", ")

the_buyers = len(names)
buyer = random.randint(0, the_buyers - 1) #need to put -1 because the iteration of a list begins with 0 not with 1
print(f"{names[buyer]} is going to buy the meal today! :D")