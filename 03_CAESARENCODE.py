# V1 inital atempet
# V2 fixing output
# V3 loopup method trial

# imports
import string as s
import sys

# constant(global) varibles
shift = 13
ExtChar = s.ascii_lowercase + s.digits +  ' ' + s.punctuation

# functions
def caesarEncode(encodeinput, characters):
    userInput = input(encodeinput).lower()
    table = str.maketrans(characters, characters[shift:]+characters[:shift])
    encodeText = userInput.translate(table)
    return encodeText
    
# **************************************************************************************************
# Main
while True:
    printCaEn = caesarEncode('Please enter the message you want to encode:', ExtChar)
    print('Here is your encoded message: \n' + printCaEn)
    repeat = input('Would you like to use it again? \n [Press 1 for yes or press 2 for no]')
    if repeat == 1:
        continue
    else:
        print('Thank your for using this program!')
        sys.exit(0)