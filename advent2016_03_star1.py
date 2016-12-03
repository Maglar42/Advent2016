
print '****************************program start************************************'
# run code from cd C:\Users\Josh\Documents\Projects\Advent2016
#to run the program type python27 programname.py
#  https://en.wikipedia.org/wiki/Taxicab_geometry

with open('advent2016_03_datafile1.txt') as textFile:
    vaildCounter = 0

    for row in textFile:
        side1 = int(str(row[0]) + str(row[1]) + str(row[2]))
        side2 = int(str(row[5]) + str(row[6]) + str(row[7]))
        side3 = int(str(row[10]) + str(row[11]) + str(row[12]))
        #print row,side1,"",side2,"",side3

        if (side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1 ):
            vaildCounter += 1
    print vaildCounter
