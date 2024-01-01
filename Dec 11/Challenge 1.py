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



#This line inserts the extra columns as needed

for charIndx in range(originalRowLength-1,-1,-1):

    for line in lines:

        char = line[charIndx]

        if char != '.': break

    if char != '.': 
        continue

    for lineIndx in range(len(lines)):

        line = lines[lineIndx]

        line = line[:charIndx+1] + ['.'] + line[charIndx+1:]

        lines[lineIndx] = line



rowInsert = ['.']*len(lines[0])



#print(rowIndxInsert)

#This line insert the extra rows as needed

for rowIndx in reversed(rowIndxInsert): lines.insert(rowIndx,rowInsert)




# #These lines pad grid 

lines = [rowInsert] + lines + [rowInsert]

for lineIndx in range(len(lines)):

    lines[lineIndx] = ['.']+lines[lineIndx]+['.']




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

        PotentialPair = {str(NumberToPair),str(Nums)}

        pairs.append(PotentialPair)

        

    


    
#print(pairs)

#print(len(pairs))

#print(lines)

#print(locsDict)

SumOfDist = 0


#This section finds the combined sum of each of the smallest distances

for pair in pairs:

    pair = list(pair)

    #print(pair)

    startingGalaxyNum = pair[0]

    currentPoint = locsDict[startingGalaxyNum]

    endGalaxyNum = pair[-1]

    endingPoint = locsDict[endGalaxyNum]

    endingPointRow = endingPoint[0]

    endingPointCol = endingPoint[-1]


    numOfSteps = 0


    while currentPoint != endingPoint:

        minDist = -1

        newPoint = currentPoint

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

        numOfSteps += 1

        if newPoint == endingPoint: 
            
            #print(f"Starting Galaxy Num: {startingGalaxyNum}")

            #print(f"Ending Galaxy Num: {endGalaxyNum}")
            
            #print(f"Num of Steps: {numOfSteps}")
            
            SumOfDist += numOfSteps

            break

        currentPoint = newPoint
        

         
print(SumOfDist)











