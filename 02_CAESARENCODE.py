# V1 inital atempet
# V2 fixing output

# constant(global) varibles
shift = 13

# functions
def caesarEncode(encodeinput):
    result = ''
    caesarenInput = input(encodeinput)
    for i in range(len(caesarenInput)):
        c = encodeinput[i]
        # checkk for spaces
        if c == ' ':
            result += ' '
        # shifts every chatacter by 13
        else:
            result += chr((ord(c) + shift-97) % 26 + 97)
    return result

# **************************************************************************************************
# Main
printCaEn = caesarEncode('Please enter the message you want to encode:').lower()
print(printCaEn)