#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')
padLine = ['.'*len(lines[0])]

#pads top and bottom of grid
lines =  padLine + lines + padLine

#Create lists to distinguish between symbols, nonsymbols, and numbers
nonSymbolsList = ["0","1","2","3","4","5","6","7","8","9","."]
numbersList = nonSymbolsList[:-1]

#create empty dictionary to store numbers and their indcidies
currentNumInfo = dict() 

#create empty dictionary to store numbers and their 
currentAsteriskInfo = dict() 


#iterate through each of the lines that could contain numbers
for lineNum in range(1,len(lines)):
    
  #pad each row analyzed
  dummyLine = '.'+lines[lineNum]+'.'

  #find location of asterisks
  currentAsteriskInfo[lineNum] = []

  #find location of numbers
  currentNumInfo[lineNum] = dict()

  #stores symbol indicies for removal
  symbolIndex = set()

  #find all asterisks and numbers
  for index in range(1,len(dummyLine)):
    
    if dummyLine[index] == "*": 
      
      currentAsteriskInfo[lineNum].append(index)

    #iterate through each row to find symbols for identification of numbers
       
    if dummyLine[index] not in nonSymbolsList:
      symbolIndex.add(dummyLine[index])

    
  for element in symbolIndex:

    dummyLine = dummyLine.replace(element,'.')


    
  #find numbers on current line
  numbers = dummyLine.split('.')
  numbers = {number for number in numbers if number !=''}

  


  #iterate through numbers array to find starting index locations for each number in line
  for number in numbers:

    #Create empty array to store indicies
    numberIndicies = [] 

    #find all starting indicies of the number extracted on analyzed line
    for currentIndex in range(1,len(dummyLine)-1):

      if dummyLine.startswith(number,currentIndex) and dummyLine[currentIndex-1] + dummyLine[currentIndex + len(number)] == '..':
             
        numberIndicies.append(currentIndex)

        currentNumInfo[lineNum][int(number)] = numberIndicies
        #  print(f"Number indicies:{numberIndicies}")
                          
  if not currentAsteriskInfo[lineNum]: del currentAsteriskInfo[lineNum] 

#  if not currentNumInfo[lineNum]: del currentNumInfo[lineNum]         


#set variable to store sum
Sum = 0

#array to find gear numbers
GearsNumbers = []

for rowNum, asteriskCoords in currentAsteriskInfo.items():

  #print(rowNum)

  for asteriskCoord in asteriskCoords:

    #print(asteriskCoord)

    minCoord = asteriskCoord - 1
    maxCoord = asteriskCoord + 1

    
    asteriskRange = {coord for coord in range(minCoord,maxCoord+1)}

    #print(asteriskRange)

    for row, numInfo in currentNumInfo.items():

      minRow = rowNum-1
      maxRow = rowNum+1

      if row >= minRow and row <= maxRow:

        for number, startCoords in numInfo.items():

          for startCoord in startCoords:

            endCoord = startCoord + len(str(number))-1

            numberRange = {coord for coord in range(startCoord,endCoord+1)}

            #print(f"Number, {number} range: {numberRange}")

            if numberRange.intersection(asteriskRange):

               
            #  print(GearsNumbers)
              GearsNumbers.append(number)
        
    #print(GearsNumbers)


    if len(GearsNumbers)==2: 
      #print(GearsNumbers)
      Sum += GearsNumbers[0]*GearsNumbers[-1]

    GearsNumbers = []



#print(f"CurrentNUminfo:{currentNumInfo}")
#print(f"asteriskLocs: {currentAsteriskInfo}")

print(Sum)







    
    


    



