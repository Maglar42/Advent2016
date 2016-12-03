
print '****************************program start************************************'
# run code from cd C:\Users\Josh\Documents\Projects\Advent2016
#to run the program type python27 programname.py
#  https://en.wikipedia.org/wiki/Taxicab_geometry

with open('advent2016_01_datafile1.txt') as textFile:
    actionDirection = ''
    steps = 0
    location = [0,0]
    directionOrder = ['N','E','S','W']
    faceing = 0

    print directionOrder[faceing], location
    for row in textFile:
        steps = int(row[1:])
        actionDirection = row[0]

        print directionOrder[faceing],
        if actionDirection == 'R':
            faceing += 1
            if faceing == 4:
                faceing = 0
        if actionDirection == 'L':
            faceing -= 1
            if faceing == -1:
                faceing = 3
        print actionDirection,directionOrder[faceing],

        if faceing == 0: #North
            stepCard = 1
            stepSign = 1
        elif faceing == 1: #East
            stepCard = 0
            stepSign = 1
        elif faceing == 2: #South
            stepCard = 1
            stepSign = -1
        elif faceing == 3: #West
            stepCard = 0
            stepSign = -1
        location[stepCard] = location[stepCard] + steps * stepSign
        print steps,location
    print 'Final Answer =', location[0] + location[1], 'steps away'
