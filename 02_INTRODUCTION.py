# 1.1 welcome the user [finished]
# 1.2 instructions [current]

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

# Main

# gets user's name and welcomes
print('Hello! Welcome to the cipher program')
name = num_checker('Please enter your name: ')
print('Welcome ' + name)

# asks if the user wants to view instructions, and acts accordingly
instructions('Would you like to read the instructions, (enter "y" or "n"):')
print('program continues')
        
        