def main():
    fileName = input('What would you like ur file to be called?')
    f = open(fileName + '.txt', 'w+')

    for i in range(10):
        f.write('This is a line %d\r\n' % (i+1))

    f.close()


if __name__ == '__main__':
    main()