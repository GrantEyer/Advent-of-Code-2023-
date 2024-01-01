#import time
from math import gcd

#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')


stepPattern = lines[0].strip()

lines.pop(0)

locDict = dict()

startingLocs = []

for line in lines: 

    if line != '':

        #print(line)

        line = line.split('=')

        locIdent = line[0].strip()

        if locIdent[-1] == "A": 
            startingLocs.append(locIdent)
            #print(locIdent)



        locOptions = line[-1].strip()

        forwardParenthLoc = locOptions.index('(')

        backwardParenthLoc = locOptions.index(')')

        commaLoc = locOptions.index(',')
        
        leftOpt = locOptions[forwardParenthLoc+1:commaLoc]

        rightOpt = locOptions[commaLoc+1:backwardParenthLoc]

        locDict[locIdent] = [leftOpt.strip(),rightOpt.strip()]




indvStepsTaken = []



for startingLoc in startingLocs:

    print(startingLoc)

    currentStepPattern = stepPattern[:]

    IndvStepsTaken = 0

    while True:

        

        #print(stepPattern)
        
        currentStep = currentStepPattern[0]

        Options = locDict[startingLoc]

        if currentStep == "R":

            startingLoc = Options[-1]

        else:

            startingLoc = Options[0]

        
        IndvStepsTaken += 1


        if startingLoc[-1]== "Z": 
            #print(IndvStepsTaken)
            indvStepsTaken.append(IndvStepsTaken)
            #print(stepsTaken) 
            break


        currentStepPattern = currentStepPattern[1:] + currentStep


stepsTaken = 1

for num in indvStepsTaken:
    stepsTaken = stepsTaken*num//gcd(stepsTaken, num)   



print(stepsTaken)



# while True:

    
    
#     currentStep = stepPattern[0]


#     for startingLocIndx in range(len(startingLocs)):
    
#         startingLoc = startingLocs[startingLocIndx]
        
#         Options = locDict[startingLoc]


#         if currentStep == "R":

#             startingLocs[startingLocIndx] = Options[-1]

#         else:

#             startingLocs[startingLocIndx] = Options[0]

        
        

#     stepsTaken += 1

#     zCount = 0

#     for element in startingLocs:

#         if element[-1] == "Z": zCount += 1
        
    
    
    

#     if zCount == len(startingLocs): 
#         break
#     elif zCount: print(f"zs found:{zCount} steps={stepsTaken}")

#     stepPattern = stepPattern[1:] + currentStep


