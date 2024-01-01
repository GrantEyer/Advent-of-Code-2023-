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

#set variable to store sunm
Sum = 0


#iterate through each of the lines that could contain numbers
for lineNum in range(1,len(lines)-1):

    #pad each row analyzed
    dummyLine = '.'+lines[lineNum]+'.'

    #iterate through each row to find symbols for identification of numbers
    for i in range(len(dummyLine)):
       
        if dummyLine[i] not in nonSymbolsList:
           
            dummyLine = dummyLine.replace(dummyLine[i],'.')

    #find numbers on current line
    numbers = dummyLine.split('.')
    numbers = [number for number in numbers if number !='']
    
    #create empty dictionary to store numbers and their indcidies
    currentNumInfo = dict() 

    


  #  print(f"Dummyline:{dummyLine}")

    #Create empty array to store indicies
    numberIndicies = []

    #Create array to keep track of indicies visitied
    visitedIndicies = []

    lastIndex = 0

    #iterate through numbers array to find starting index locations for each number in line
    for index in range(len(numbers)):

        #extract number from number array
        number = numbers[index]



       # print(f"Number:{number}")

        #find all starting indicies of the number extracted on analyzed line
        for currentIndex in range(1,len(dummyLine)-1):

          #  print(f"Currentindex = {currentIndex}")
            
            if dummyLine.startswith(number,currentIndex) and dummyLine[currentIndex-1]=='.' and dummyLine[currentIndex + len(number)]=='.':
              #  print("In here")
                lastIndex = currentIndex + len(numbers[index]) - 1
              #  print(f"Before:{numberIndicies}")
                numberIndicies.append([currentIndex, lastIndex])

                currentNumInfo[int(number)] = numberIndicies
              #  print(f"Number indicies:{numberIndicies}")
            else:
                lastIndex += 1
                         
        #Create empty array to store indicies
        numberIndicies = []


                 


    if not currentNumInfo: continue




    linesAnalyzed = ['.'+ Line + '.' for Line in lines[lineNum-1:lineNum+2]]

    indiciesSymbols = dict()

    for num in range(len(linesAnalyzed)):

        indiciesSymbols[num] = []

        Line = linesAnalyzed[num]

        for index in range(len(Line)):

            if Line[index] not in nonSymbolsList:

                indiciesSymbols[num].append(index)


    flagToAdd = False

    for number,numCoords in currentNumInfo.items():
      #  print(number,numCoord)

      for [minCoord,maxCoord] in numCoords:

        for symbolCoords in indiciesSymbols.values():

            for i in range(0,len(symbolCoords)):

                symbolCoord = symbolCoords[i]

                if symbolCoord >= minCoord-1 and symbolCoord <= maxCoord+1:

                    flagToAdd = True
            

        if flagToAdd: 
          #  print(f"Number added: {number}")

            Sum += number
            flagToAdd = False

  #  print(linesAnalyzed)
  #  print(numberIndicies)
  #  print(indiciesSymbols)
  #  print(f"CurrentNUminfo:{currentNumInfo}")

print(Sum)







    
    


    



