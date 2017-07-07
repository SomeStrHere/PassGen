# Program to generate a password and output it to the console.
# V: 0.9.0

import random
from os import urandom
from random import choice
import sys

def userInput() :
    """Asks user what length of password to create."""

    try : 
        userLength = int(input('How many characters would you like in your password? '))
    except : 
            print('Sorry there was an error')
            # TODO
    
    return(userLength)

def generateRandom() : 
    """Generate random characters to form a password."""

    charsets = [
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '0123456789',
        '^!\$%&/()=?{[]}+~#-_.:,;<>|\\',
        ]

    length = userInput()
    pwd = []
    charset = choice(charsets)
    while len(pwd) < length:
        pwd.append(choice(charset))
        charset = choice(list(set(charsets) - set([charset])))
    return outputPassword("".join(pwd))


def outputPassword(passwordString) :
    """Output password to user."""

    print('\nThank you for using PassGen')
    print('This is your password: {0}\n'.format(passwordString))

def main() : 
    
    generateRandom()

if __name__ == "__main__" :
    main()

