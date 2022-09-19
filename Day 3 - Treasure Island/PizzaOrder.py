# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"

# What size pizza do you want?
# Do you want pepperoni?
# Do you want extra cheese?

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 13:
#       bill = 5
#       print(f"Child ticket price is $5.")
#   elif age <= 18:
#       bill = 7
#       print(f"Youth ticket price is $7.")   
#   else:
#       bill = 12
#       print(f"Adult ticket price is $12.")
        
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#       bill += 3

#   print(f"Your final bill is ${bill}.")
        
        
# else:
#     print("Alexa, play 'Short people got no reason to live'")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
bill = 0

print("***Welcome to Micheal's Pizza Palace!***\nSmall Pizza = $15\nMedium Pizza = $20\nLarge Pizza = $25\nAdd Pepperoni = $2 for Small & $3 for Medium or Large\nExtra Cheese for any pizza = $1")
user_pizza_size = input("What size pizza do you want? S, M, or L ")
user_pepperoni_choice = input("Do you want pepperoni? Y or N ")
user_extra_cheese_choice = input("Do you want extra cheese? Y or N ")


if user_pizza_size == "S" or "s":
  bill = 15
  if user_pepperoni_choice == "Y" or "y":
    bill += 2
  if user_extra_cheese_choice == "Y" or "y":
    bill += 1
elif user_pizza_size == "M" or "m":
  bill = 20
  if user_pepperoni_choice == "Y" or "y":
    bill += 3
  if user_extra_cheese_choice == "Y" or "y":
    bill += 1
else: 
  bill = 25 
  if user_pepperoni_choice == "Y" or "y":
    bill += 3
  if user_extra_cheese_choice == "Y" or "y":
    bill += 1   
print(f"Your bill is: ${bill}.")
