# if condition:
#   do this
# else:
#   do this
# == - exact match - checking equality



# user_height = input("What is your height in inches? ")

# if int(user_height) >= 52:
#     print("You can ride today.")
# else:
#     print("Alexa, play 'short people got no reason to live'")
    
    # Nested If/Else
    # Once first condition is passed, checks for another condition
# if condition:
    # if another condition:
#       do this (requires both prior conditions)
# else:
#   do this (requires one prior condition)

height = int(input("What is your height? "))
age = int(input("What is your age? "))
youth_ticket = 7
adult_ticket = 12
child_ticket = 5

if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 13:
        print(f"Your ticket price is ${child_ticket}")
    elif age <= 18:
        print(f"Your ticket price is ${youth_ticket}")   
    else:
        print(f"Yout ticket price is {adult_ticket}")
else:
    print("Alexa, play 'Short people have no reason to live'")