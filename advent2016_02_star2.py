
print '****************************program start************************************'
# run code from cd C:\Users\Josh\Documents\Projects\Advent2016
#to run the program type python27 programname.py
#  https://en.wikipedia.org/wiki/Taxicab_geometry

with open('advent2016_02_datafile1.txt') as textFile:
    code = ''
    currentButton = [2,0]
    priorButton = [0,0]
    buttonGrid = [['*','*','1','*','*'],['*','2','3','4','*'],['5','6','7','8','9'],['*','A','B','C','*'],['*','*','D','*','*']]
                # **1**
                # *234*
                # 56789
                # *ABC*
                # **D**
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

            priorButton[0] = currentButton[0]
            priorButton[1] = currentButton[1]

            currentButton[moveDirection[0]] = currentButton[moveDirection[0]] + moveDirection[1]

            if (currentButton[0] == -1 or currentButton[1] == -1 or currentButton[0] == 5 or currentButton[1] == 5):
                 currentButton[0] = priorButton[0]
                 currentButton[1] = priorButton[1]
            elif (buttonGrid[currentButton[0]][currentButton[1]] == "*"):
                 currentButton[0] = priorButton[0]
                 currentButton[1] = priorButton[1]

            if char != '\n':
                print char, moveDirection, priorButton,currentButton
            else:
                print buttonGrid[currentButton[0]][currentButton[1]]

        code += str(buttonGrid[currentButton[0]][currentButton[1]])
        print '\n'

    print 'Final Button:', code
