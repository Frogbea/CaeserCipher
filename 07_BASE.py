# v0 This is the setup version
# v1 adding the introduction component
# v2 changing the introduction component to the username/password option
# v3 adding the caesar encoder
# v4 adding the caesar decoder
# v5 adding playfair encoder
# v6 adding playfair decoder
# v7 final version

# imports
import json as j, os, os.path, sys as s
import msvcrt as m, string as st

# Global/constant varible set-up
error_highlight = '*****'
boxDeco = '******************************************'
userName = ['initial value']
password = ['inital value']
filename = 'storeUser.json'
shift = 13
ExtChar = st.ascii_lowercase + st.digits +  ' ' + st.punctuation
playkey = 'poise'

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
            print('{} \n >>>> The encryption and decryption processes used in this program are unique! This means that if you encode something using this program, it can only be decoded using this program. \n \n >>>> Your username and password are both stored so please do not enter any personal details, and remember to make your password unique. \n \n >>>> Make sure to read the prompts before selecting 1 for yes or 2 for no (dont worry about remembering that, its said in every question). \n \n >>>> If you do not know what the Playfair or Caesar ciphers are (or want to learn more about them) please vist this link: https://en.wikipedia.org/wiki/Playfair_cipher for the Playfair cipher or this one: https://en.wikipedia.org/wiki/Caesar_cipher for the Caesar cipher. \n \n >>>> You can input anything into the caesar cipher, but the playfair cipher does not encode numbers, puncuation, or spaces. Enjoy! :) \n {}'.format(boxDeco, boxDeco))
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
    i = 3
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
        print('Please enter your new password below [Please do not make it the same as your username!!]:')
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
    # creates table and encodes message
    userInput = input(encodeinput).lower()
    table = str.maketrans(characters, characters[shift:]+characters[:shift])
    encodeText = userInput.translate(table)
    return encodeText

def caesardecode(decodeInput, characters):
    # creates table and decodes message
    caesarInput = input(decodeInput)
    newShift = -shift
    table = str.maketrans(characters, characters[newShift:]+characters[:newShift])
    translated_text = caesarInput.translate(table)
    return translated_text

# functions for playfair cipher
def noNum(Ninput):
    # makes sure user does not enter any numbers
    while True:
        noNumInput = input(Ninput).replace(' ', '')
        if any(char.isdigit() for char in noNumInput):
            print('{}Please do not enter any numbers{}'.format(error_highlight, error_highlight))
            continue
        else:
            break
    return noNumInput

def matrixKey(key):
    # sets boundries for matrix
    key = key.upper()
    matrix = [[0 for i in range (5)] for j in range(5)]
    charAdd = []
    row = 0
    col = 0
    # add key word to matrix
    for letter in key:
        # add key word to the top of the matrix
        if letter not in charAdd:
            matrix[row][col] = letter
            charAdd.append(letter)
        else:
            continue
        # cuts off column at four
        if (col == 4):
            col = 0
            row += 1
        # makes new column when column does not equal 4
        else:
            col += 1
    # add rest of alphebet to matrix
    for letter in range(65, 91):
        # take out j playfair only uses 25 letters
        if letter == 74:
            continue
        # add letter if its not already there
        if chr(letter) not in charAdd:
            charAdd.append(chr(letter))
        index = 0
    # cutes off each column
    for i in range(5):
        for j in range(5):
            matrix[i][j] = charAdd[index]
            index += 1
    return matrix

def sameChar(message):
    index = 0
    # checks if there is any double or lone characters
    while index < len(message):
        l1 = message[index]
        # if this is the last character
        if index == len(message) - 1:
            message = message + 'X'
            index += 2
            break
        l2 = message[index + 1]
        # if 2 consewcutive characters
        if l1 == l2:
            message = message[:index + 1] + 'X' + message[index + 1:]
            index += 2
        else:
            index += 1
    return message

def index(letter, matrix):
    # for the rules
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return(i, index)
        except:
            continue

def playfair(key, message, playDecode):
    # set up the key and message
    inc = 1
    # for decodeing
    if playDecode:
        inc = -1
    matrix = matrixKey(key)
    message = sameChar(message)
    cipherText = ''
    # checks every 2nd character, putting them in the pairs
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1, col1 = index(l1, matrix)
        row2, col2 = index(l2, matrix)
        # rule one
        if row1 == row2:
            cipherText += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
        # rule two
        elif col1 == col2:
            cipherText += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
        # rule three
        else:
            cipherText += matrix[row1][col2] + matrix[row2][col1]
    return cipherText

# ****************************************************************************************************
# Main program
if __name__ == '__main__':
    # setting up the file/information for storing usernames
    jSetup()
    # Welcome user
    print('Hello! Welcome to the cipher program.')

    # asks if the user wants to view instructions, and acts accordingly
    instructions('Would you like to read the instructions, (enter "y" or "n"):')

    # ask for previous user
    prevUser = user12('Do you *already* have a username and password?\n [Press 1 for yes or press 2 for no]:')
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
            newUserName = user12('[Press 1 for yes or press 2 for no]:')
            # if yes welcome the user
            if newUserName:
                print('Welcome back!')
            # if no force to make a new username
            else:
                print('You need to make a new username to continue.')
                createStoreUser()
        newPass()
        print('Password creation successful. Welcome to the program!')
    # loop for cipher codes
    while True:
        # ask if user wants to encrypt or depcrypt
        enDc = user12('Would you like to encode or decode a message? \n [Press 1 to encode message or press 2 to decode it]:')
        # encodes if value is true 
        if enDc:
            # ask user which cipher
            enCipher = user12('Would you like to encode using the Caesar cipher or the Playfair cipher? \n [Press 1 for Caesar or press 2 for Playfair]:')
            # if true caeser
            if enCipher:
                # caesar encode loop
                printCaEn = caesarEncode('Please enter the message you want to encode:', ExtChar)
                print('Here is your encoded message: \n {} \n {} \n {}'.format(boxDeco, printCaEn, boxDeco))
            # if false playfair
            else:
                # playfair encode loop
                orgInput = noNum('Please enter the message you would like to encode:')
                playFairEn = orgInput.translate(str.maketrans('', '', st.punctuation)).replace(' ', '').upper()
                answer = playfair(playkey, playFairEn, False)
                print('Here is your encoded message: \n {} \n {} \n {}'.format(boxDeco, answer, boxDeco))
        # decodes if value is false
        else:
            dcCipher = user12('Would you like to decode using the Caesar cipher or the Playfair cipher? \n [Press 1 for Caesar or press 2 for Playfair]:')
            if dcCipher:
                # caesar decoding code
                caesarOutput = caesardecode('Please enter the encrypted message that you want to decode:', ExtChar)
                print('Here is your decoded message: \n {} \n {} \n {}'.format(boxDeco, caesarOutput, boxDeco))
            else:
                # playfair decoding code
                playDc = noNum('Please enter the message you would like to decode:').upper()
                result = playfair(playkey, playDc, True)    
                print('Here is your decoded message: \n {} \n {} \n {}'.format(boxDeco, result.lower(), boxDeco))
        # code to repeat the whole thing
        repeat = user12('Would you like to use this again? \n [Press 1 for yes or press 2 for no]:')
        if repeat:
            continue
        else:
            print('Thank you for using this program!')
            s.exit(0)
