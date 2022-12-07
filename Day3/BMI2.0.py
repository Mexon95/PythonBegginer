height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / (height ** 2)

rounded_BMI = round(BMI)

if rounded_BMI < 18.5:
    print(f"Your BMI is {rounded_BMI}, you are underweight.")
elif 18.5 <= rounded_BMI < 25:
    print(f"Your BMI is {rounded_BMI}, you have a normal weight.")
elif 25 <= rounded_BMI < 30:
    print(f"Your BMI is {rounded_BMI}, you are slightly overweight.")
elif 30 <= rounded_BMI < 35:
    print(f"Your BMI is {rounded_BMI}, you are obese.")
else:
    print(f"Your BMI is {rounded_BMI}, you are clinically obese.")