#
# Number generator for a number-guessing game.
#
import random

def get_number(max):
    '''
    Returns a randomly generated number in the range 1 through max.
    '''
    number = random.randrange(1, max + 1)
    return number
