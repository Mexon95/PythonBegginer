year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print("Leap year.")
elif year % 100 != 0:
    print("Not leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
    
    
#second version:
#if year % 4 == 0:
#   if year % 100 == 0:
#       if year % 400 == 0:
#           print("Leap year")
#       else:
#           print("Not leap year")
#   else:
#       print("Leap year.")
#else:
#   print("Not a leap year")
