# Program to generate a password and output it to the console.
# V: 1.0.0

from os import urandom
from random import choice
import math
import sys

def userInput() :
    """Asks user what length of password to create."""

    userLength=0

    user_input = input('How many characters would you like in your password? ')

    accepted, user_input = checkInput(user_input)

    if not accepted :
        print('Sorry, there was an error')
        input('Press the enter key to exit')
        sys.exit()

    return user_input

def checkInput(usr_input, recursive=True) :
    local_user_input = usr_input
    accepted = False
    try:
        int(local_user_input)
        accepted = True
    except ValueError as e:
        if recursive :
            local_user_input = input("Incorrect input. Please enter a number: ")
            accepted, local_user_input = checkInput(local_user_input, False)

    if accepted :
        local_user_input = int(local_user_input)

    return accepted, local_user_input



def generateRandom() : 
    """Generate random characters to form a password."""

    charSets = [
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '0123456789',
        '^!\$%&/()=?{[]}+~#-_.:,;<>|\\',
        ]

    length = userInput()
    pwd = []
    charset = choice(charSets)

    while len(pwd) < length :

        pwd.append(choice(charset))
        charset = choice(list(set(charSets) - set([charset])))

    return outputPassword("".join(pwd))
        

def outputPassword(passwordString) :
    """Output password to user."""

    print('\nThank you for using PassGen')
    print('This is your password: {0}\n'.format(passwordString))


def main() : 
    
    generateRandom()

if __name__ == "__main__" :
    main()
    