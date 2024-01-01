#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

NumberOfGalaxies = 0



rowIndxInsert = []

#This line numbers the galaxies

for lineIndx in range(len(lines)):

    line = list(lines[lineIndx])

    if line.count("#") > 0:
    
        for charIndx in range(len(line)):

            char = line[charIndx]
            
            if char == "#":

                NumberOfGalaxies += 1

                line[charIndx] = str(NumberOfGalaxies)

    else:

        rowIndxInsert.append(lineIndx)

    lines[lineIndx] = line


originalRowLength = len(lines[0])



millionCols = []

#This line detects where extra column would occur

for charIndx in range(originalRowLength):

    for line in lines:

        char = line[charIndx]

        if char != '.': break

    if char != '.': 
        continue

    millionCols.append(charIndx)





rowInsert = ['.']*len(lines[0])


# #These lines pad grid 

lines = [rowInsert] + lines + [rowInsert]

for lineIndx in range(len(lines)):

    lines[lineIndx] = ['.']+lines[lineIndx]+['.']






        



#determine which rows represent a million rows
millionRow = [rowNum+1 for rowNum in rowIndxInsert]

millionCols = [colNum + 1 for colNum in millionCols]



locsDict = {}

# #This section finds locations of galaxies
for rowNum in range(len(lines)):

    line = lines[rowNum]
    
    for colNum in range(len(line)):

        char = line[colNum]
        
        if char != '.':

            locsDict[char] = [rowNum,colNum]



# #This section finds unique pairings
pairs = []


NumberList = list(range(1,NumberOfGalaxies+1))

NumberListLength = len(NumberList)





while NumberList:

    NumberToPair = NumberList.pop(0)

    #print(NumberToPair)

    for Nums in NumberList:

        PotentialPair = [str(NumberToPair),str(Nums)]

        pairs.append(PotentialPair)
    
#print(pairs)

#print(len(pairs))

#print(lines)

#print(millionCols)

#print(millionRow)

#print(locsDict)

SumOfDist = 0

WorthofEmptyRows = 1e6

WorthOfEmptyCols = WorthofEmptyRows


#This section finds the combined sum of each of the smallest distances

for pair in pairs:

    pair = list(pair)

    #print(pair)

    startingGalaxyNum = pair[0]

    currentPoint = locsDict[startingGalaxyNum]

    #print(f"StartingPoint:{currentPoint}")

    endGalaxyNum = pair[-1]

    endingPoint = locsDict[endGalaxyNum]

    #print(f"StartingPoint:{endingPoint}")

    endingPointRow = endingPoint[0]

    endingPointCol = endingPoint[-1]


    numOfSteps = 0


    while currentPoint != endingPoint:

        minDist = -1

        newPoint = currentPoint

        prevRow = newPoint[0]

        prevCol = newPoint[-1]

        for direction in ["North","South","East","West"]:

            row = currentPoint[0]

            col = currentPoint[-1]

            match direction:

                case "North": row -= 1
                
                case "South": row += 1

                case "East": col += 1

                case "West": col -= 1


            #calculate distance to end galaxy
            distSq = (row-endingPointRow)**2+(col-endingPointCol)**2

            dist = (distSq)**(1/2)

            if minDist == -1 or dist < minDist: 
                
                minDist = dist
                newPoint = [row,col]

        
        row = newPoint[0]

        col = newPoint[-1]

        if row in millionRow and prevRow != row:

            #print(f"newpoint on multirow: {newPoint}")

            numOfSteps += WorthofEmptyRows
        
        
        elif col in millionCols and prevCol != col:


            #print(f"newpoint on multicolumn: {newPoint}")

            numOfSteps += WorthofEmptyRows

        else:
            #print(f"newpoint not on multirow or column: {newPoint}")
            numOfSteps += 1

        if newPoint == endingPoint: 
            
            #print(f"Starting Galaxy Num: {startingGalaxyNum}")

            #print(f"Ending Galaxy Num: {endGalaxyNum}")
            
            #print(f"Num of Steps: {numOfSteps}")
            
            SumOfDist += numOfSteps

            break

        currentPoint = newPoint
        

         
print(SumOfDist)











