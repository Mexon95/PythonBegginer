number = int(input("Which number do you want to check? "))
remainder = number % 2

if remainder == 0: # this if statement could have been if number % 2 == 0; so it coul be done without creating the object remainder
    print("This is an even number.")
else:
    print ("This is an odd number.")