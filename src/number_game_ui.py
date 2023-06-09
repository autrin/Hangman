#
# User interface for the number_game module
#

import number_game
import numbers

def play_game():
		print("Guess a number between 1 and 10")
		secret = numbers.get_number(10)
		number_game.start(secret, 3)
		while not number_game.is_over():
				guess = int(input("Enter a guess: "))
				hint = number_game.guess_number(guess)
				print(hint)
				if (number_game.is_won()):
						print("You win!")
				elif number_game.is_over():
						print("Sorry, you lost.")
				else:
						print("You have " + str(number_game.guesses_left()) + " guesses left")
        
# execution starts here
play_game()

    
