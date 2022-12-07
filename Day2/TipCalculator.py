#Greeting
print("Welcome to the tip calculator")
#Total bill
total_bill = float(input("What was the total bill? "))
#Tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#No of people
number_of_people = int(input("How many people to split the bill? "))
#Calculate the tip from the total bill
tip_total = total_bill * (tip_percentage / 100)
#How much an individual has to pay
must_pay = (total_bill + tip_total) / number_of_people
rounded_sum = round(must_pay, 2)
print(f"Each person should pay: {rounded_sum}")