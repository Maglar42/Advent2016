
print '****************************program start************************************'
# run code from cd C:\Users\Josh\Documents\Projects\Advent2016
#to run the program type python27 programname.py
#  https://en.wikipedia.org/wiki/Taxicab_geometry

with open('advent2016_03_datafile1.txt') as textFile:
    vaildCounter = 0
    triangleList = []
    swappedTriangleList = []
    rowCounter = 0

    for row in textFile:
        side1 = int(str(row[0]) + str(row[1]) + str(row[2]))
        side2 = int(str(row[5]) + str(row[6]) + str(row[7]))
        side3 = int(str(row[10]) + str(row[11]) + str(row[12]))
        #print row,side1,"",side2,"",side3
        triangleList.append([side1,side2,side3])
        rowCounter += 1

    for i in xrange(0,rowCounter,3):
        for j in range(0,3):
            swappedTriangleList.append([triangleList[i][j],triangleList[i+1][j],triangleList[i+2][j]])

    for t in swappedTriangleList:
        if (t[0] + t[1] > t[2]  and t[0] + t[2] > t[1] and t[2] + t[1] > t[0]):
            vaildCounter += 1
    print vaildCounter
