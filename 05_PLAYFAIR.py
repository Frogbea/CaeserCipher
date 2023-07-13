# v1 making the matrix
# v2 removing spaces and puncuation from inputs
# v3 rejecting numbers
# v4 making encoder
# v5 tidying up & testing
#imports

import string as st

#constants
playkey = 'poise'

#functions

def noNum(Ninput):
    while True:
        noNumInput = input(Ninput).replace(' ', '')
        if any(char.isdigit() for char in noNumInput):
            print('Please do not enter any numbers')
            continue
        else:
            break
    return noNumInput

def matrixKey(key):
    print('matrix start')
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
    print('matrix finish')
    return matrix

def sameChar(message):
    print('Samechar start')
    index = 0
    while index < len(message):
        l1 = message[index]
        if index == len(message) - 1:
            message = message + 'X'
            index += 2
            print('if last character is reached')
            break
        l2 = message[index + 1]
        if l1 == l2:
            message = message[:index + 1] + 'X' + message[index + 1:]
            index += 2
            print('x added to same char')
        else:
            index += 1
        print('loop continued')
    print('sameChar finish')
    return message

def index(letter, matrix):
    print('indexstart')
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            ('index finish')
            return(i, index)
        except:
            ('In loop')
            continue

def playEncode(key, message):
    print('encode start')
    inc = -1
    matrix = matrixKey(key)
    message = sameChar(message)
    cipherText = ''
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1, col1 = index(l1, matrix)
        row2, col2 = index(l2, matrix)
        if row1 == row2:
            print('first rule')
            cipherText += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
        elif col1 == col2:
            print('second rule')
            cipherText += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
        else:
            print('third rule')
            cipherText += matrix[row1][col2] + matrix[row2][col1]
    print('encode finish')
    return cipherText


#***************************************************************************************************
#MAIN
# this is the key table for the cipher
print('test')
orgInput = noNum('Please enter the message you would like to encode:')
print('test1')
playFairEn = orgInput.translate(str.maketrans('', '', st.punctuation)).replace(' ', '').upper()
print('test2')
answer = playEncode(playkey, playFairEn)
print('test3')
print('this is the message: ' + answer)


