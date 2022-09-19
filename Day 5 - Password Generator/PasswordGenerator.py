import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the MS Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

endrange_letter = len(letters) - 1
endrange_number = len(numbers) - 1
endrange_symbols = len(symbols) - 1

pw_letters = ""
for number in range(0, nr_letters):
    randomletter = letters[random.randint(0, endrange_letter)]
    pw_letters += f"{randomletter}"
# print(pw_letters)

pw_numbers = ""
for number in range(0, nr_numbers):
    randomnumber = numbers[random.randint(0, endrange_number)]
    pw_numbers += f"{randomnumber}"
# print(pw_numbers)

pw_symbols = ""
for number in range(0, nr_symbols):
    randomsymbol = symbols[random.randint(0, endrange_symbols)]
    pw_symbols += f"{randomsymbol}"
# print(pw_symbols)

easy_password = pw_letters + pw_numbers + pw_symbols
print(f"Your easy password is {easy_password}")

# **************

hard_list = list(easy_password)
endrange_hard = len(hard_list) - 1

random_hard = ""
for number in range(0, len(hard_list)+ 1):
    random_hard_letter = hard_list[random.randint(0, endrange_hard) - 1]
    random_hard += f"{random_hard_letter}"
print(f"Your hard password is {random_hard}")

    



    



