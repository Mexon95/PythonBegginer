print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

total_score = 0
both_names = name1.lower() + name2.lower()

T_score = both_names.count('t')
R_score = both_names.count('r')
U_score = both_names.count('u')
E_score = both_names.count('e')
true = T_score + R_score + U_score + E_score

L_score = both_names.count('l')
O_score = both_names.count('o')
V_score = both_names.count('v')
E_score = both_names.count('e')
love = L_score + O_score + V_score + E_score

total_score = str(true) + str(love) # or total_score = int(str(true) + str(love))  

if int(total_score) < 10 or int(total_score) > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif int(total_score) > 40 and int(total_score) < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")