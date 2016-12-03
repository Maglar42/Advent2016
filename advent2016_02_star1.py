
print '****************************program start************************************'
# run code from cd C:\Users\Josh\Documents\Projects\Advent2016
#to run the program type python27 programname.py
#  https://en.wikipedia.org/wiki/Taxicab_geometry

with open('advent2016_02_datafile1.txt') as textFile:
    code = ''
    currentButton = [1,1]
    buttonGrid = [[1,2,3],[4,5,6],[7,8,9]]
                #123
                #456
                #789
    moveDirection = [0,0] #first is x or y second is positive or negative


    for row in textFile:
        for char in row:
            moveDirection = [0,0]
            if char == "U":
                moveDirection = [0,-1]
            elif char == "D":
                moveDirection = [0,1]
            elif char == "L":
                moveDirection = [1,-1]
            elif char == "R":
                moveDirection = [1,1]
            elif char == '\n':
                print 'end of line'

            print currentButton,
            currentButton[moveDirection[0]] += moveDirection[1]
            if currentButton[0] == -1:
                currentButton[0] = 0
            if currentButton[0] == 3:
                currentButton[0] = 2
            if currentButton[1] == -1:
                currentButton[1] = 0
            if currentButton[1] == 3:
                currentButton[1] = 2

            if char != '\n':
                print char, currentButton
            else:
                print buttonGrid[currentButton[0]][currentButton[1]]

        code += str(buttonGrid[currentButton[0]][currentButton[1]])
        print '\n'

    print 'Final Button:', code
