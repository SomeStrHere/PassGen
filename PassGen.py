# Program to generate a password and output it to the console.
# V: 1.0.0

from os import urandom
from random import choice
import math
import sys

def userInput() :
    """Asks user what length of password to create."""

    userLength=0

    try : 
        userLength = int(input('How many characters would you like in your password? '))

    except :
        print('\nSorry there was an error')
        print('Please try again...')

        try : 
            userLength = int(input('\nHow many characters would you like in your password? '))
        except : 

            print('Sorry, there was an error')
            input('Press any key to exit')
            sys.exit()
                       
    return(userLength)


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
    