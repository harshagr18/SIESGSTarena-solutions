# Problem Link : 
#Enter the code to create a random number guessing game.
import random
import math
# Here we take the Lower Input from the user and use try-catch to see if the Input
#entered is an integer.
#If it is not an integer the user is prompted again to enter a valid Integer.
while True:
  try:
    lower = int(input("Enter lower bound: "))
    if lower > 0:
      break
    print("Invalid number entered, Please enter an integer")
  except Exception as e:
    print(e)

# Here we take the Upper Input from the user and use try-catch to see if the Input
#entered is an integer.
#If it is not an iteger the user is prompted to enter a valid Integer.
while True:
  try:
    upper = int(input("Enter upper bound: "))
    if upper > 0:
      break
    print("Invalid number entered, Please enter an integer")
  except Exception as e:
    print(e)

# Here we use the randint from the random module to generate a random
#number between the lower and the upper limit.
numb = random.randint(lower, upper)

# Here, we initialize the number of guessess to 0.
count = 0

# Now, here we run the while loop until the correct number is guesses by the user.
while 1:
	count += 1

	# Here we take the user input for the number guessed
	guess = int(input("Guess a number:- "))

	# If the user guessess it correctly we display that message
	if numb == guess:
		print("Congratulations you did it in ",
			count, " tries")
		# Here, once the correct number is guessed, We break from the loop.
		break
	#Here, if the guess is smaller than the random number generated,
	#we tell the user to  guess a larger number
	elif numb > guess:
		print("You guessed too small! Please Guess a higher number")
	#Here if the guess is larger than the random number generated,
	#we tell the user to guess a smaller number.
	elif numb < guess:
		print("You Guessed too high! Please guess a smaller number")



