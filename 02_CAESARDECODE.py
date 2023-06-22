# v1 inital attempt
# v2 repeat code

# imports
import string as s

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
caesarOutput = caesardecode('Please enter the encrypted message that you want to decode:', ExtChar)
print('Here is your decoded message:\n', caesarOutput)