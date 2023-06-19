# T0 this is the first option - nothing
# T1 this is the second option -just username
# T2 the is the third option - username and password

# imports
import json as j, os, os.path, sys as s
from getpass import getpass

# Global varible set-up
error_highlight = '*****'
userName = ['initial value']
password = ['inital value']
filename = 'storeUser.json'

# Functions

def jSetup():
    # creating new file is user doesn't have one
    if not os.path.exists(filename):
        with open(filename, mode='w') as f:
            j.dump(userName, f)
    # making list readable for json file
    jDump = j.dumps(userName)
    jData = j.loads(jDump)

def instructions(yesNo):
    # loop checks what the user chooses and acts accordingly
    while True:
        instrucView = input(yesNo).lower()
        if instrucView == 'y':
            print('here are the instructions')
            break
        elif len(instrucView) == 0:
            print('{}Please enter "y" for yes or "n" for no!{}'.format(error_highlight, error_highlight))
        elif instrucView == 'n':
            break
        else:
            print('{}Please enter "y" for yes or "n" for no!{}'.format(error_highlight, error_highlight))
    return 

def user12(message):
    while True:
        # try & except to catch erros
        try:
            enDcinput = int(input(message))
            # sets to true if user picks encode
            if enDcinput == 1:
                return True
                break
            # sets to false if user picks decode
            elif enDcinput == 2:
                return False
                break
            else:
                print('{}Please enter 1 or 2!{}'.format(error_highlight, error_highlight))
        except:
            # prints error if user does anything else
            print('{}Please enter 1 or 2!{}'.format(error_highlight, error_highlight))

def createStoreUser():
    # reads previous data
    file = open(filename, 'r')
    userName = j.load(file)
    file.close()
    # creates new username
    createUser = input('Please create a username:')
    # if username already exsists doesn't make a new one
    if createUser in userName:
        print('User {} already exsits. Would you like to log in as {}?'.format(createUser, createUser))
        return True
    else:
        userName.append(createUser)
        # adds new username to file
        file = open(filename, 'w')
        j.dump(userName, file)
        file.close()
        print('Welcome to the program {}'.format(createUser))
        return False

def checkPrevUser(message):
    # while loop 5 times
    i = 5
    while i >= 0:
        prevUserInput = input(message)
        # reads information in file
        with open(filename, 'r') as file:
            data = j.load(file)
        # checks if username is in data
        if prevUserInput in data:
            print("Welcome back {} it's good to see you again".format(prevUserInput))
            prevUserInput = True
            break
        # if they don't get it they have to repeat
        else:
            print('{}Sorry that username is not in the database, you have {} attempts left{}'.format(error_highlight, i, error_highlight))
            prevUserInput = False
            i -= 1
    return prevUserInput

def enterpass():
    pass

def newPass(passInput):
    # reads previous data
    file = open(filename, 'r')
    password = j.load(file)
    file.close()
    # creates and dumps new password
    createNewPass = getpass(passInput)
    password.append(createNewPass)
    file = open(filename, 'w')
    j.dump(password, file)
    file.close()

# **********************************************
# Main program
if __name__ == '__main__':
    # setting up the file/information for storing usernames
    jSetup()
    # Welcome user
    print('Hello! Welcome to the cipher program')

    # ask for previous user
    prevUser = user12('Do you already have a username and password?\n [Press 1 for yes or press 2 for no]')
    # if yes ask to enter it
    if prevUser:
        prevUserBoolen = checkPrevUser('Please enter your username:')
        # if they don't get it in 5 tries
        if not prevUserBoolen:
            quitCreate = user12('Would you like to create a new username? \n [Press 1 for yes or press 2 for no]')
            # creates new user
            if quitCreate:
                createStoreUser()
            # ends program
            else:
                print('You must have a username to use this program! \n Ending program..!')
                s.exit(0)
        else:
            enterPass = enterpass('Please enter your password:')
    # helps user create new username
    else:
        # create new user
        create = createStoreUser()
        # if user already exsists
        if create:
            # gets user input
            newUserName = user12('[Press 1 for yes or press 2 for no]')
            # if yes welcome the user
            if newUserName:
                print('Welcome back!')
            # if no force to make a new username
            else:
                print('You need to make a new username to continue.')
                createStoreUser()
        createpass = newPass('Please enter your new password:')

    # asks if the user wants to view instructions, and acts accordingly
    instructions('Would you like to read the instructions, (enter "y" or "n"):')
    print('program continues')

    # ask if user wants to encrypt or depcrypt
    enDc = user12('Would you like to encode or decode a message? \n [Press 1 to encode message or press 2 to decode it]:')
    # encodes if value is true 
    if enDc:
        # ask user which cipher
        enCipher = user12('Would you like to encode using the Caser cipher or the Playfair cipher? \n [Press 1 for Caeser (sn) or press 2 for Playfair]:')
        # if true caeser
        if enCipher:
            print('caeser(sn) encode')
        # if false playfair
        else:
            print('playfair encode')
    # decodes if value is false
    else:
        dcCipher = user12('Would you like to decode using the Caser cipher or the Playfair cipher? \n [Press 1 for Caeser (sn) or press 2 for Playfair]:')
        if dcCipher:
            print('caeser(sn) decode')
        else:
            print('playfair decode')
