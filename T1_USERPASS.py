# T0 this is the first option 
# T1 this is the second option

# imports
import json as j
import os
import os.path
import sys as s

# Global varible set-up
error_highlight = '*****'
userName = ['initial value']
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
        except ValueError:
            # prints error if user does anything else
            print('{}Please enter 1 or 2!{}'.format(error_highlight, error_highlight))

def createStoreUser():
    # reads previous data
    file = open(filename, 'r')
    userName = j.load(file)
    file.close()
    # creates new username
    createUser = input('Please create a username:')
    userName.append(createUser)
    # adds new userna,e to file
    file = open(filename, 'w')
    j.dump(userName, file)
    file.close()

def checkPrevUser(message):
    i = 5
    while i >= 0:
        prevUserInput = input(message)
        with open(filename, 'r') as file:
            data = j.load(file)
        if prevUserInput in data:
            print("Welcome back {} it's good to see you again".format(prevUserInput))
            prevUserInput = True
            break
        else:
            print('{}Sorry that username is not in the database, you have {} attempts left{}'.format(error_highlight, i, error_highlight))
            prevUserInput = False
            i -= 1
    return prevUserInput

# **********************************************
# Main program
# setting up the file/information for storing usernames
jSetup()
# Welcome user
print('Hello! Welcome to the cipher program')

# ask for previous user
prevUser = input('Do you already have a username?').lower()
if prevUser == 'yes':
    prevUserBoolen = checkPrevUser('Please enter your username')
    if not prevUserBoolen:
        quitCreate = user12('Would you like to create a new username? \n [Press 1 for yes or press 2 for no]')
        if quitCreate:
            createStoreUser()
        else:
            print('Ending program..!')
            s.exit(0)
elif prevUser == 'no':
    createStoreUser()

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