import random

print("Welcome to Guess the Number!" + '\n' + "The rules are simple. I will think of a number, and you will try to guess it." + '\n')
#print("The rules are simple. I will think of a number, and you will try to guess it." + '\n')

print("Welcome to Guess the Number!" + '\n')
print("The rules are simple. I will think of a number, and you will try to guess it." + '\n')

number = random.randint(1,10)
isGuessRight = False

#Starts while loop, takes input (guess), and if user input matches randomization (number) it will output win message and end loop. Else, continues user input guesses.
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
