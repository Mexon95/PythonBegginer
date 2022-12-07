age = input("What is your current age? ")
years_left = 90 - int(age)
days_left = int(years_left) * 365
weeks_left = int(years_left) * 52
months_left = int(years_left) * 12
# f-String - write at the beggining of the string an f and all of the int, float, bool, etc are written in curly brackets
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")