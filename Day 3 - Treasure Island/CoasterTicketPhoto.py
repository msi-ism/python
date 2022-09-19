bill = 0
height = int(input("What is your height? "))


if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 13:
      bill = 5
      print(f"Child ticket price is $5.")
  elif age <= 18:
      bill = 7
      print(f"Youth ticket price is $7.")  
  elif age >= 45 and age <= 55:
      print("We'll all float on. Have a ride on us.")
  else:
      bill = 12
      print(f"Adult ticket price is $12.")
        
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
      bill += 3

  print(f"Your final bill is ${bill}.")
        
        
else:
    print("Alexa, play 'Short people got no reason to live'")