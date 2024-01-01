import math

#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

pipeMap = {}

startingIndx = []

padding = ["."*len(lines[0])]

lines = padding + lines + padding

for rowNum in range(len(lines)):

    line = "." + lines[rowNum] + "."
    
    
    if "S" in line: 

        columnNum = line.index("S")

        startingIndx.extend([rowNum,columnNum])


    pipeMap[rowNum] = line


pipeMapCopy = pipeMap.copy()

currentLocation = startingIndx

previousLocation = ""

oppositeDirection = ""

loopArray = []

options = {"F":{"South","East"},"7":{"West","South"},
           "|":{"North","South"},"-":{"East","West"},
           "J":{"North","West"},"L":{"North","East"},
           "S":{"North","South","East","West"}}



possibleDirections = ["North","South","East","West"]

#i=0
#find main loop first before finding distance
while loopArray.count(startingIndx) != 2:

    rowCoord = currentLocation[0]

    columnCoord = currentLocation[-1]

    currentChar = pipeMap[rowCoord][columnCoord]

    #print(f"Starting Loc:{currentLocation}")

    potentialCoords = {}
    
    for direction in possibleDirections:

        match direction:

            case "North":
                possibleRowCoord = rowCoord - 1
                possibleColumnCoord = columnCoord
            
            case "South":
                possibleRowCoord = rowCoord + 1
                possibleColumnCoord = columnCoord

            case "East":
                possibleRowCoord = rowCoord
                possibleColumnCoord = columnCoord + 1

            case "West":
                possibleRowCoord = rowCoord
                possibleColumnCoord = columnCoord - 1

        if [possibleRowCoord,possibleColumnCoord] != previousLocation and direction in options[currentChar]:

            potentialCoords[direction] = [possibleRowCoord,possibleColumnCoord]



    #print(f"Coords as options:{potentialCoords}")
         
    deadEnds = 0
    
    for [possibleRowCoord,possibleColumnCoord] in potentialCoords.values():

        #print(f"Possible next coord:{[possibleRowCoord,possibleColumnCoord]}")
        
        characterAhead = pipeMap[possibleRowCoord][possibleColumnCoord] 

        

        if characterAhead == "S":

            #print("Branch 1")

            loopArray.append([rowCoord,columnCoord])

            loopArray.append([possibleRowCoord,possibleColumnCoord])
            
            break

  
        elif characterAhead in options.keys():

            #print("Branch 2")


            #moving south, coming from the north
            if possibleRowCoord - rowCoord > 0:

                oppositeDirection = "North"

            elif possibleRowCoord - rowCoord < 0:

                oppositeDirection = "South"

            elif possibleColumnCoord - columnCoord > 0:

                oppositeDirection = "West"

            else:

                oppositeDirection = "East"

            #print(oppositeDirection)
        
            if oppositeDirection in options[characterAhead]:

                #print("Branch 2 Sub 1") 

                loopArray.append(currentLocation)

                previousLocation = currentLocation

                currentLocation = [possibleRowCoord,possibleColumnCoord]
                
                break

        else:

            #print("Branch 3") 

            deadEnds += 1

    
    if deadEnds == 4:

        #print("Going bACK")
        oldStringBefore = pipeMap[possibleRowCoord][:possibleColumnCoord]
        oldStringAfter = pipeMap[possibleRowCoord][possibleColumnCoord+1:]

        pipeMap[possibleRowCoord] = oldStringBefore + '.' + oldStringAfter

        loopArray.pop()
        currentLocation = loopArray[-1]
        previousLocation = loopArray[-2]


#loopArray.pop()



endLoc = loopArray[-2]

startLoc = loopArray[1]

#find what character "S" is

coordsArr = [startLoc,endLoc]

directionsUsed = set()
    
for [rowNum,colNum] in coordsArr:

    if rowNum - startingIndx[0] < 0:

        directionsUsed.add("North")

    elif rowNum - startingIndx[0] > 0:

        directionsUsed.add("South")

    elif colNum - startingIndx[-1] > 0:

        directionsUsed.add("East")

    else:

        directionsUsed.add("West")

values = list(options.values())

characters = list(options.keys())

charIndx = values.index(directionsUsed)
    
char2replace = characters[charIndx]

#rteplace S character with appropriate element
originalLine = pipeMapCopy[startingIndx[0]]

originalLine = originalLine.replace("S",char2replace)

pipeMapCopy[startingIndx[0]] = originalLine

rowInfo = {}

for rowNum,elements in pipeMapCopy.items():

    columnInfo = []
    
    for col in range(len(elements)):

        if [rowNum,col] in loopArray:

            columnInfo.append(col)
    
    rowInfo[rowNum] = sorted(columnInfo)


#print(rowInfo)


InsideArea  = 0

#HorizDirection = "West"

for rowNum, columnInfo in rowInfo.items():

    if columnInfo:

        InsideLoop = True

        InsideSet = set()

        StartingColumnNum = columnInfo[0]

        for Indx in range(1,len(columnInfo)):

            #print(f"Inside Loop {InsideLoop}")

            NextColumnNum = columnInfo[Indx]


            NextChar = pipeMapCopy[rowNum][NextColumnNum]

            StartingChar = pipeMapCopy[rowNum][StartingColumnNum]

            #if HorizDirection not in options[NextChar] or "North" in options[NextChar] or "South" in options[NextChar]


            if NextChar != '-':

                #if these character combinations exist, it means that the status of being in or out of the loop hasn't changed.


                
                if (NextChar == "J" or NextChar == "L") and StartingChar == "F": 
                    
                    
                    pass


                elif (NextChar == "7" or NextChar == "F") and StartingChar == "L": 
                    
                    
                    pass
                
                else:                   

                    
                    if InsideLoop and NextColumnNum-StartingColumnNum>1:
                        
                        #print(f"Inside Loop") 

                        #print(rowNum)

                        #print(StartingColumnNum)

                        #print(NextColumnNum)

                        #print(pipeMapCopy[rowNum][StartingColumnNum:NextColumnNum+1])     
                        
                        for colNum in range(StartingColumnNum+1,NextColumnNum):

                            if colNum not in columnInfo:

                                InsideSet.add(colNum)

                    InsideLoop = not InsideLoop

                    StartingColumnNum = NextColumnNum

        InsideArea += len(InsideSet)




            
print(f"InsideArea = {InsideArea}")


