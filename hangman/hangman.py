#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karen
#
# Created:     23/11/2012
# Copyright:   (c) Karen 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import random
import linecache

def main():
    pass

def picture_print(case):
    if case == 0:
        print ""
        print "  -----"
        print "  |   |"
        print "      |"
        print "      |"
        print "      |"
        print "      |"
        print "      |"
        print "  ---------"
        print ""

    elif case == 1:
        print ""
        print "  -----"
        print "  |   |"
        print "  O   |"
        print "      |"
        print "      |"
        print "      |"
        print "      |"
        print "  ---------"
        print ""

    elif case == 2:
        print ""
        print "  -----"
        print "  |   |"
        print "  O   |"
        print "  |   |"
        print "  |   |"
        print "      |"
        print "      |"
        print "  ---------"
        print ""

    elif case == 3:
        print ""
        print "  -----"
        print "  |   |"
        print "  O   |"
        print " -|   |"
        print "  |   |"
        print "      |"
        print "      |"
        print "  ---------"
        print ""

    elif case == 4:
        print ""
        print "  -----"
        print "  |   |"
        print "  O   |"
        print " -|-  |"
        print "  |   |"
        print "      |"
        print "      |"
        print "  ---------"
        print ""

    elif case == 5:
        print ""
        print "  -----"
        print "  |   |"
        print "  O   |"
        print " -|-  |"
        print "  |   |"
        print "_/    |"
        print "      |"
        print "  ---------"
        print ""

    elif case == 6:
        print ""
        print "  -----"
        print "  |   |"
        print "  O   |"
        print " -|-  |"
        print "  |   |"
        print "_/ \_ |"
        print "      |"
        print "  ---------"
        print ""
    return

def secret_word():
    word_num = random.randrange(0,112504)
    word_line = linecache.getline('C:\Users\Richard\Google Drive\Engineering\Python\hangman\infl.txt', word_num)
    word = word_line.split()
    word = word[0]
    return word

def letter_replacement(guess):
    counter = 0
    wrong_letter = 0
    while counter<word_length:
        if word_full[counter] == guess:
            word_blanks[counter] = guess
            wrong_letter = 1
        counter += 1
    return wrong_letter

def continue_game():
    game = str(raw_input("Continue Playing the Game [y/n]: "))
    if game == 'y':
        game = 1
    else:
        game = 0
    return game

def word_level(level):
    word_full = secret_word()
    word_length = len(word_full)

    if level == '1':
        while word_length > 4:
            word_full = secret_word()
            word_length = len(word_full)
    elif level == '2':
        while word_length <= 4 and word_length > 10:
            word_full = secret_word()
            word_length = len(word_full)
    else:
        while word_length <= 10:
            word_full = secret_word()
            word_length = len(word_full)
    return  word_full

def dash_counter():
    counter = 0
    dashes = 0
    while counter < word_length:
        if word_blanks[counter] == '-':
            dashes += 1
        counter += 1
    return dashes


def game_play():
    dashes = dash_counter()
    case = 0

    while dashes > 0 and case < 6:
        guess = str(raw_input("Guess a letter: "))
        guess = guess.lower()
        status = letter_replacement(guess)

        if status == 0:
            print 'letter was not found'
            case += 1
            picture_print(case)
        else:
            print 'letter found!'
            picture_print(case)

        word_current = ''
        counter = 0
        while counter < word_length:
            word_current = word_current + word_blanks[counter]
            counter += 1
        print word_current

        dashes = dash_counter()

    if case < 6:
        print 'congratulations! you won!'
    else:
        print ''
        print 'you lost. you are so pathetic. you are such a failure.'
        print 'the word was: {0}'.format(word_full)
        print ''

    return

##program start

if __name__ == '__main__':
    main()

case = 0
game = 1

while game != 0:
    picture_print(case)
    print "welcome to hangman...your worst nightmare"
    level = str(raw_input("select level [1-3]: "))

    word_full = word_level(level)
    word_full = word_full.lower()
    word_length = len(word_full)
    word_blanks = ['-'] * word_length
    game_play()
    game = continue_game()