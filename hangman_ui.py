# User interface for the hangman module.

import hangman
import words


def select_game_and_word():
    '''
    Shows the menu and let us choose from 3 different collections of words.
    '''
    choice = input('Which version of the game would you like to play?\na) Kitchen utensils\nb) Farm animals\nc) '
                   'Word from file')
    while (choice != 'a') and (choice != 'b') and (choice != 'c'):
        print('Please enter a, b, or c')
        choice = input(
            'Which version of the game would you like to play?\na) Kitchen utensils\nb) Farm animals\nc) '
            'Word from file ')
    if choice == 'a':
        return words.get_kitchen_word()
    elif choice == 'b':
        return words.get_special_word()
    elif choice == 'c':
        return words.get_word_from_file('word_list.txt')


def display_game():
    '''
    Prints out the current state of the game, including a stick
    figure drawn under a scaffold.
    '''
    stick_figure = ['/', '\\', '|', '\\', '/', 'o']
    positions = [34, 35, 26, 27, 25, 18]
    health = max(0, 6 - hangman.get_guesses_left())
    scaffold = list( \
        "  ____ \n" + \
        "  1   |\n" + \
        "      |\n" + \
        "      |\n" + \
        "      |\n" + \
        "=======\n")

    for x in range(health):
        scaffold[positions[x]] = stick_figure[x]
    print("".join(scaffold))
    print("Word so far:    " + " ".join(hangman.get_displayed_word()))
    print("Letters already guessed: " + ", ".join(hangman.get_guessed_letters()))
    print("You have " + str(hangman.get_guesses_left()) + " guesses left")


def play_game():
    '''
    Plays one round of the hangman game.
    '''
    print("Welcome to Com S 127 Hangman")

    hidden = select_game_and_word()
    hangman.start(hidden, 6)
    while not hangman.is_over():
        display_game()
        letter = input("Enter your guess: ")
        correct = hangman.guess_letter(letter)
        if correct:
            print("Good guess!")
        else:
            print("Nope.")
        if hangman.is_won():
            display_game()
            print("You won!")
        elif hangman.is_over():
            display_game()
            print("Sorry, you've lost.")

    print("The word was " + hangman.get_hidden_word())


# Execution starts here
play_game()
