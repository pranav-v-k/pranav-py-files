#Guess the Number Game

#import random module
import random

#Generate random number
random_number = random.randint(1,20)

#Intro message
print("Welcome to the Guess the Number Game!")
print("I am thinking of a number between 1 and 20. Can you guess it?")

#Looping until the correct guess
while True:
    #get user input
    user_guess = int(input("Please enter your guess: "))
    #Check if the user guessed correctly
    if user_guess == random_number:
        print("You guessed it right! The number was indeed {}".format(random_number))
        break
    else:
        #If the guess is too low or too high
        if user_guess > random_number:
            print("Your guess is too high!")
        else:
            print("Your guess is too low!")