# v1 doing decoder

# imports
import json as j, os, os.path, sys as s
import msvcrt as m, string as st

# constant
playkey = 'poise'

# functions

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



# MAIN
playDc = input('Please enter the message you would like to decode:').upper()
result = playfair(playkey, playDc, True)    
print('Here is your decoded message: \n' + result)