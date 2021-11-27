myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type" + str(type(myString)) + '\n')

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString + '\n')

name = input("What's your name? ")
print(name + '\n')

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))