# input() will get user input in console
# Then print() will print the word "Hello" and the user input
# print("Hello " + input("What is your name?") + "!")

# ltr = sets variable which is users input
# str(len(name.replace(" ", ""))) - takes "name" variable and converts to string, len(finds length of string, name.replace(" ", ""))) - replaces spaces with nothing to give true count)
name = (input("Tell me your name and I'll tell you how many letters are in it! "))
print("Hello " + (str(name)) + ", your name has " + str(len(name.replace(" ", ""))) + " letters!")