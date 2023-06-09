
# Module containing the state of a hangman game and
# related functions for playing the game.

# The hidden word
hidden_word1 = ''
# The displayed word as a list of characters
displayed_word = []
# The letters that have already been guessed, as a list of characters
guessed_letters = []
# The number of guesses the player has left
guesses_left = 0
# The maximum number of the guesses
max_guess = 0


def start(hidden_word, max_guesses):
    '''
    Starts the game.
    Does not return anything. Creates the displayed word based on the number of the letters in the hidden word.
    '''
    global hidden_word1, displayed_word, max_guess, guesses_left
    hidden_word1 = hidden_word
    max_guess = max_guesses
    guesses_left = max_guess
    displayed_word = ['-'] * len(hidden_word)


def guess_letter(letter):
    '''
    Returns True if the letter is in the hidden word and not in the letter that has been guessed. Display the correct
    guessed letter in the displayed word. Subtracts 1 from the number of the guesses has left.
    '''
    global guesses_left, guessed_letters, hidden_word1
    if (letter in hidden_word1) and (letter not in guessed_letters):
        for i in range(len(hidden_word1)):
            if letter == hidden_word1[i]:
                displayed_word[i] = letter
        guessed_letters.append(letter)
        return True
    else:
        guesses_left -= 1
        guessed_letters.append(letter)
        return False


def get_displayed_word():
    '''
    :return: the displayed word
    '''
    return displayed_word


def get_hidden_word():
    '''
    :return: the hidden word
    '''
    global hidden_word1
    return hidden_word1


def get_guesses_left():
    '''
    :return: the number of the guesses has been left
    '''
    global guesses_left
    return guesses_left


def get_guessed_letters():
    '''
    :return: the list of the guessed letters
    '''
    global guessed_letters
    return guessed_letters


def is_over():
    '''
    :return: true if the game is over, meaning the played cannot guess anymore or has guessed the hidden word
    '''
    new_word = ''.join(get_displayed_word())
    if guesses_left == 0 or new_word == hidden_word1:
        return True
    else:
        return False


def is_won():
    '''
    :return: True if the player has won, meaning the game has completed and the word has been guessed correctly. And
    return false if not.
    '''
    new_word = ''.join(get_displayed_word())
    if is_over() == True and new_word == hidden_word1:
        return True
    else:
        return False
