#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

stepPattern = lines[0].strip()

lines.pop(0)

locDict = dict()

startingLoc = ''

for line in lines: 

    if line != '':

        #print(line)

        

        line = line.split('=')

        locIdent = line[0].strip()

        if locIdent == "AAA": startingLoc = locIdent



        locOptions = line[-1].strip()

        forwardParenthLoc = locOptions.index('(')

        backwardParenthLoc = locOptions.index(')')

        commaLoc = locOptions.index(',')
        
        leftOpt = locOptions[forwardParenthLoc+1:commaLoc]

        rightOpt = locOptions[commaLoc+1:backwardParenthLoc]

        locDict[locIdent] = [leftOpt.strip(),rightOpt.strip()]


stepsTaken = 0


while True:

    #print(stepPattern)
    
    currentStep = stepPattern[0]

    Options = locDict[startingLoc]

    if currentStep == "R":

        startingLoc = Options[-1]

    else:

        startingLoc = Options[0]

    
    stepsTaken += 1


    if startingLoc == "ZZZ": break


    stepPattern = stepPattern[1:] + currentStep

print(stepsTaken)