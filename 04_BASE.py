# v0 This is the setup version
# v1 adding the introduction component
# v2 changing the introduction component to the username/password option
# v3 adding the caesar encoder
# v4 adding the caesar decoder

# imports
import json as j, os, os.path, sys as s
import msvcrt as m, string as st

# Global/constant varible set-up
error_highlight = '*****'
userName = ['initial value']
password = ['inital value']
filename = 'storeUser.json'
shift = 13
ExtChar = st.ascii_lowercase + st.digits +  ' ' + st.punctuation

# Functions

# setup/general functions
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

def userWrong():
    # asks if user would like to make new one because didn't get username in 5 tries
    quitCreate = user12('Would you like to create a new username & password? \n [Press 1 for yes or press 2 for no]')
    # creates new user
    if quitCreate:
        createStoreUser()
        newPass()
        print('Password created successfully! Welcome :)')
    # ends program
    else:
        print('You must have a username & password to use this program! \n Ending program..!')
        s.exit(0)

# functions for usernames
def createStoreUser():
    # reads previous data
    file = open(filename, 'r')
    userName = j.load(file)
    file.close()
    while True:
        # creates new username
        createUser = input('Please create a username:')
        if len(createUser) != 0:
            break
        print('{}Please enter a username!{}'.format(error_highlight, error_highlight))
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
            print("Welcome {} it's good to see you again".format(prevUserInput))
            prevUserInput = True
            break
        # if they don't get it they have to repeat
        else:
            print('{}Sorry that username is not in the database, you have {} attempts left{}'.format(error_highlight, i, error_highlight))
            prevUserInput = False
            i -= 1
    return prevUserInput

# functions for passwords
def enterpass():
    i = 3
    while i >= 0:
        print('Please enter your password below:')
        checkUserPass = hidePass()
        # opens & reads file
        with open(filename, 'r') as file:
            data = j.load(file)
        # checks password is correct
        if checkUserPass in data:
            print('That password was correct! Welcome back :)')
            checkUserPass = True
            break
        else:
            print('{}Sorry that password is not correct, you have {} tries left{}'.format(error_highlight, i, error_highlight))
            checkUserPass = False
            i -= 1
    return checkUserPass

def hidePass():
    password = ''
    if s.stdin.isatty():
        while True:
            # gathers each individual character using getch
            char = m.getch()
            # if enter key break loop, save password
            if ord(char) == 13:  # Enter key
                if len(password) == 0:
                    print('{}Please make a password:'.format(error_highlight))
                    continue
                print()
                break
            # if backspace delete
            elif ord(char) == 8:  # Backspace key
                if len(password) > 0:
                    password = password[:-1]
                    s.stdout.write("\b \b")
            # replaces characters with *
            else:
                password += char.decode("utf-8")
                s.stdout.write("*")
    return password

def newPass():
    # reads previous data
    file = open(filename, 'r')
    password = j.load(file)
    file.close()
    while True:
        # creates and dumps new password
        print('Please enter your new password below [please do not add any personal data & makesure to remeber your password!]:')
        createNewPass = hidePass()
        if createNewPass in password:
            print('{}This password already exists please enter a new one!{}'.format(error_highlight, error_highlight))
        else:
            password.append(createNewPass)
            file = open(filename, 'w')
            j.dump(password, file)
            file.close()
            break

# functions for caeser cipher
def caesarEncode(encodeinput, characters):
    userInput = input(encodeinput).lower()
    table = str.maketrans(characters, characters[shift:]+characters[:shift])
    encodeText = userInput.translate(table)
    return encodeText

def caesardecode(decodeInput, characters):
    caesarInput = input(decodeInput)
    newShift = -shift
    table = str.maketrans(characters, characters[newShift:]+characters[:newShift])
    translated_text = caesarInput.translate(table)
    return translated_text

# ****************************************************************************************************
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
        # user enters username
        prevUserBoolen = checkPrevUser('Please enter your username:')
        # if they don't get it in 5 tries
        if not prevUserBoolen:
            userWrong()
        else:
            enterPass = enterpass()
            if not enterPass:
                userWrong()
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
        newPass()
        print('Password creation successful. Welcome to the program!')

    # asks if the user wants to view instructions, and acts accordingly
    instructions('Would you like to read the instructions, (enter "y" or "n"):')

    # ask if user wants to encrypt or depcrypt
    enDc = user12('Would you like to encode or decode a message? \n [Press 1 to encode message or press 2 to decode it]:')
    # encodes if value is true 
    if enDc:
        # ask user which cipher
        enCipher = user12('Would you like to encode using the Caesar cipher or the Playfair cipher? \n [Press 1 for Caesar or press 2 for Playfair]:')
        # if true caeser
        if enCipher:
           # caesar encode loop
           while True:
            printCaEn = caesarEncode('Please enter the message you want to encode:', ExtChar)
            print('Here is your encoded message: \n' + printCaEn)
            repeat = user12('Would you like to use it again? \n [Press 1 for yes or press 2 for no]')
            # Ceasar encode repeat
            if repeat:
                continue
            else:
                print('Thank your for using this program!')
                s.exit(0)
        # if false playfair
        else:
            print('playfair encode')
    # decodes if value is false
    else:
        dcCipher = user12('Would you like to decode using the Caesar cipher or the Playfair cipher? \n [Press 1 for Caesar or press 2 for Playfair]:')
        if dcCipher:
            # caesar decoding code
            while True:
                caesarOutput = caesardecode('Please enter the encrypted message that you want to decode:', ExtChar)
                print('Here is your decoded message:\n', caesarOutput)
                repeatDc = user12('Would you like to use it again?\n[Press 1 for yes or press 2 for no]')
                # repeat code
                if repeatDc:
                    continue
                else:
                    print('Thank you for using this program!')
                    s.exit(0)
        else:
            print('playfair decode')
