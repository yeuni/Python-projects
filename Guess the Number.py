#The Goal: User input random number until he/she guesses right, 
 
#The program will 
# first randomly generate a
#  number unknown to the user.
#  The user needs to guess what 
# that number is. (In other words,
#  the user needs to be able to input information.)
#  If the user’s guess is wrong, the program should 
# return some sort of indication as to how wrong 
# (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
#Concepts to keep in mind:

#Random function
#Variables
#Integers
#Input/Output
#Print
#While loops
#If/Else statements

# This is a guess the number game.

import random

user_number_of_Guesses = 0
number = random.randint(1,20)

name = input("Tsup! What is your name? ")

print(name + ", I am thinking of a whole number between 1 and 20. Can you guess what it is?")

while user_number_of_Guesses < 5:
  guess = input("Take a guess ")
  guess = int(guess)

  user_number_of_Guesses = user_number_of_Guesses + 1
  guessesLeft = 5 - user_number_of_Guesses

  if guess < number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too low! You have " + guessesLeft + " guesses left")

  if guess > number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too high! You have " + guessesLeft + " guesses left")

  if guess==number:
    break

if guess==number:
  user_number_of_Guesses=str(user_number_of_Guesses)
  print("Excellent job! You guessed the number in " + user_number_of_Guesses + " tries :)")

if guess!=number:
  number=str(number)
  print("MMhhh! Sorry. The number I was thinking of was " + number)
