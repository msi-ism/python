a = input("a. ")
b = input("b. ")
# written this way to show how python stores values
# You can replace a variable with a new variable and then use that old variable to hold something new
c = a
a = b
b = c
print("a. " + str(a))
print("b. " + str(b))