# v1 inital attempt
# v2 repeat code

# imports
import string as s
import sys

# constant(global) varibles
shift = 13
ExtChar = s.ascii_lowercase + s.digits +  ' ' + s.punctuation

# fucntions
def caesardecode(decodeInput, characters):
    caesarInput = input(decodeInput)
    newShift = -shift
    table = str.maketrans(characters, characters[newShift:]+characters[:newShift])
    translated_text = caesarInput.translate(table)
    return translated_text

# ********************************************************************
# Main
while True:
    caesarOutput = caesardecode('Please enter the encrypted message that you want to decode:', ExtChar)
    print('Here is your decoded message:\n', caesarOutput)
    repeatDc = int(input('Would you like to use it again?\n[Press 1 for yes or press 2 for no]'))
    if repeatDc == 1:
        continue
    else:
        print('Thank you for using this program!')
        sys.exit(0)