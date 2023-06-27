# v1 making the matrix
# v2 removing spaces and puncuation from inputs
# v3 rejecting numbers
#imports

import string as st

#constants
key = 'poise'

#functions
def matrixKey(key):
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

#***************************************************************************************************
#MAIN
# this is the key table for the cipher
Matrix = matrixKey(key)

orgInput = input('Please enter the message you would like to encode:').replace(' ', '')
playFairEn = orgInput.translate(str.maketrans('', '', st.punctuation))
print(playFairEn)
