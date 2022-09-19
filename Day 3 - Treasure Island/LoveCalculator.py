# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1 + name2

true_name = combined_name.lower().replace(' ', '')

t_count = true_name.count("t")
r_count = true_name.count("r")
u_count = true_name.count("u")
e_count = true_name.count("e")

l_count = true_name.count("l")
o_count = true_name.count("o")
v_count = true_name.count("v")
e_count = true_name.count("e")

true_score = t_count + r_count + u_count + e_count
love_score = l_count + o_count + v_count + e_count

total_score = str(true_score) + str(love_score)

if int(total_score) < 10 or int(total_score) > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif int(total_score) > 40 and int(total_score) < 50: 
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
    
# true_count = []
# love_count = []