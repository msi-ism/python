import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

end_range = len(names) - 1
bill_payer = random.randint(0, end_range)

print(names[bill_payer] + " is going to buy the meal today!")

print(names)