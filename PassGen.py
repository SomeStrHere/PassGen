# Program to generate a password and output it to the console.
# V: 1.0.0

from os import urandom
from random import choice
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


def splitOutput(passwordString) :
    """Split output into seperate lines of 10 characters."""

    # We assume here that x is an int and > 0

    #x = 10
    #size = len(passwordString)
    #chunkSize = size//x # // truncates a float to avoid file type error

    #for pos in range(0, size, chunkSize):
    #    yield passwordString[pos:pos+chunkSize]
    upper = 10
    lower = 0

    for steps in range(len(passwordString)) :
        string = passwordString[lower:upper]
        print(string)
        upper = upper + upper
        lower = lower + 10
        

def outputPassword(passwordString) :
    """Output password to user."""

    print('\nThank you for using PassGen')
    print('This is your password: {0}\n'.format(passwordString))

    # Trying to implement a new line to the string after every 10 characters

    splitOutput(passwordString)
    

def main() : 
    
    generateRandom()

if __name__ == "__main__" :
    main()
    