# 1.1 welcome the user [finished]
# 1.2 instructions [finished]
# 1.3 which cipher encode/decode [current]

# global (constant?) varibles
error_highlight = '*****'

# function
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

# Main

# gets user's name and welcomes
print('Hello! Welcome to the cipher program')
name = num_checker('Please enter your name: ')
print('Welcome ' + name)

# asks if the user wants to view instructions, and acts accordingly
instructions('Would you like to read the instructions, (enter "y" or "n"):')
print('program continues')

# ask if user wants to encrypt or depcrypt
enDc = userEnDc('Would you like to encode or decode a message? \n [Press 1 for encode or press 2 for decode]')
# encodes if value is true 
if enDc:
    print('encode')
# decodes if value is false
else:
    print('decode')