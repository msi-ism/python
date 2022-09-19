print("Welcome to the world's best Tip Calculator.")
bill = input("What was the total bill? ")
tip_10 = 10
tip_12 = 12
tip_15 = 15
percentage = input(f"What percentage tip would you like to give? {tip_10}, {tip_12}, or {tip_15}? ")
party_size = input("How many people to split the bill? ")
tip_split = (float(bill)) * (int(percentage) * .01) / int(party_size)
print(f"Each person should pay: ${round(tip_split,2)}")