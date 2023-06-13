error_highlight = '*****'

def num_checker(nameInput):
    while True:
        nameStr = input(nameInput)
        if any(char.isdigit() for char in nameStr):
            print('{}Please do not add integers{}'.format(error_highlight, error_highlight))
        elif len(nameStr) == 0:
            print('{}Please enter a name!{}'.format(error_highlight, error_highlight))
        else:
            break
    return nameStr
        

print('Hello! Welcome to the cipher program')
name = num_checker('Please enter your name: ')
print('Welcome ' + name)