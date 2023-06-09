#
# Module for a number-guessing game
#

# The secret number
secret_number = None

# Number of times the player has already guessed
guesses = None

# Maximum number of guesses for this game
max_guesses = None

# Whether or not the player won
won = None

def start(secret, max):
    '''
    Starts a new game with the given secret number and maximum number of guesses.
    '''
    # We need to initialize all the global variables at the start of each round
    global secret_number, max_guesses, guesses, won
    secret_number = secret
    guesses = 0
    max_guesses = max
    won = False

def guess_number(guess):
    '''
    Checks the given guess and returns an appropriate message.
    '''
    global guesses, won
    guesses += 1
    if guess == secret_number:
        won = True
        return "That's it!"
    elif guesses == max_guesses:
        return "The number was " + str(secret_number)
    elif guess < secret_number:
        return "Too low."
    else:
        return "Too high"
    
def is_won():
    '''
    Returns True if the player has won the game, false otherwise.
    '''
    return won

def is_over():
    '''
    Returns True if the game has ended, false otherwise.
    '''
    return won or guesses == max_guesses

def guesses_left():
    '''
    Returns the number of guesses the player has left.
    '''
    return max_guesses - guesses
        
