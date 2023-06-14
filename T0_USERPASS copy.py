# T0 this is the first option 

# Global varible set-up
error_highlight = '*****'

# Functions
def num_checker(nameInput):
    # checks that the user doesn't input any numbers, and doesn't leave it blacnk
    while True:
        nameStr = input(nameInput)
        if any(char.isdigit() for char in nameStr):
            print('{}Please do not add integers{}'.format(error_highlight, error_highlight))
        elif len(nameStr) == 0:
            print('{}Please enter a name!{}'.format(error_highlight, error_highlight))
        else:
            break
    return nameStr

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

def userEnDc(message):
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

def cipherChoice(choice):
    while True:
        # try & except to catch erros
        try:
            caplinput = int(input(choice))
            # sets to true if user picks caeser
            if caplinput == 1:
                return True
                break
            # sets to false if user picks playfair
            elif caplinput == 2:
                return False
                break
        except ValueError:
            # prints error if user does anything else
            print('{}Please enter 1 or 2!{}'.format(error_highlight, error_highlight))


# **********************************************
# Main program

# Welcome user ask for name
print('Hello! Welcome to the cipher program')
name = num_checker('Please enter your name: ')
print('Welcome ' + name)

# asks if the user wants to view instructions, and acts accordingly
instructions('Would you like to read the instructions, (enter "y" or "n"):')
print('program continues')

# ask if user wants to encrypt or depcrypt
enDc = userEnDc('Would you like to encode or decode a message? \n [Press 1 to encode message or press 2 to decode it]:')
# encodes if value is true 
if enDc:
    # ask user which cipher
    enCipher = cipherChoice('Would you like to encode using the Caser cipher or the Playfair cipher? \n [Press 1 for Caeser (sn) or press 2 for Playfair]:')
    # if true caeser
    if enCipher:
        print('caeser(sn) encode')
    # if false playfair
    else:
        print('playfair encode')
# decodes if value is false
else:
    dcCipher = cipherChoice('Would you like to decode using the Caser cipher or the Playfair cipher? \n [Press 1 for Caeser (sn) or press 2 for Playfair]:')
    if dcCipher:
        print('caeser(sn) decode')
    else:
        print('playfair decode')