# Program to generate a password and output it to the console.
# V: 1.0.0

from os import urandom
from random import choice
import sys

def userInput() :
    """Asks user what length of password to create."""

    userLength=1

    try : 
        userLength = int(input('How many characters would you like in your password? '))
    except : 
            print('\nSorry there was an error')
            userErrorChoice()
    
    return(userLength)


def userErrorChoice() :
    """Asks user if they want to try again or exit."""
    
    userChoice = input('Type (A) to try again or (X) to quit:' ).upper()

    if userChoice == 'A' :
        generateRandom()

    elif userChoice == 'X' :
        sys.exit()

    else :
        clearConsole(0)
        userErrorChoice() #repeats question until user answers A or X


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


def clearConsole(wait) : #function to clear console on Linux or Windows
    """Clears console, with optional time delay.

    Will attempt to clear the console for Windows, should that fail it will attempt to clear the
    console for Linux.
    """

    import time
    time.sleep(wait) 
    # produces a delay based on the argument given to clearConsole()
    
    import os

    try :
       os.system('cls') #clears console on Windows

    except :
       os.system('clear') #clears console on Linux

def main() : 
    
    generateRandom()

if __name__ == "__main__" :
    main()

