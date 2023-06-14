# T0 this is the first option 
# T1 this is the second option

# imports
import shelve as s

# Global varible set-up
error_highlight = '*****'

# Functions

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
shelve_file = s.open('storeUsername')

# Welcome user
print('Hello! Welcome to the cipher program')

# creating a username
userName = []
createUser = input('Please create a username: ')
userName.append(createUser)
shelve_file['userName'] = userName
shelve_file.close()

shelve_file = s.open('storeUsername')

# print old data
print(f'Old Data = {shelve_file["userName"]}')

# update data 
shelve_file['userName'] = userName

# print updated data 
print(f'Updated Data = {shelve_file["userName"]}')

# to make changes permanent
shelve_file.sync()

# now, we simply close the shelf file.
shelve_file.close()

# pulling old usernames
shelve_file = s.open('storeUsername')
oldUser = shelve_file['userName']
shelve_file.close()
print(oldUser)


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