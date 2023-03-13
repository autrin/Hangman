# Word generator for a letter-guessing game.
import random


def get_kitchen_word():
    '''
    Returns a randomly selected word from a list of the names
    of kitchen items.
    '''
    word_list = ["spoon", "fork", "spatula", "toaster", "knife", "griddle", "oven", "pot", "skillet", "bowl"]
    index = random.randrange(0, len(word_list))
    return word_list[index]


def get_special_word():
    '''
    Returns a randomly selected word from a list defined by the programmer.
    '''
    word_list = ['sheep', 'pig', 'cow', 'chicken', 'goat', 'turkey', 'cattle']
    index = random.randrange(0, len(word_list))
    return word_list[index]


def get_word_from_file(filename):
    '''
    Returns a randomly selected word from the given file.
    '''
    return random.choice(open(filename).readlines())
