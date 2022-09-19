height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."

bmi =  (weight) / float(height ** 2)

if bmi > 31:
    print(f"Your bmi is {round(bmi,2)}, you are obese.")
elif bmi > 25:
        print(f"Your bmi is {round(bmi,2)}, you are slightly overweight.")
elif bmi >= 18.5:
            print(f"Your bmi is {round(bmi)}, you have a normal weight.")
elif bmi < 18.5:
        print(f"Your bmi is {round(bmi,2)}, you are underweight.")
else:
    print(f"Your bmi is {round(bmi,2)}, you are clinically obese.")

# if bmi < 18.5:
#     print(f"Your bmi is {round(bmi,2)}, you are obese")
    