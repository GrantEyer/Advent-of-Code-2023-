import time

#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

springCondInfo = []

#print(len(lines))

for line in lines:



    lineRevised = line.split(' ')

    #print(line)

    listNums = lineRevised[-1].split(',')

    #print(listNums)

    listNums = [int(num) for num in listNums if num != '']

    springCondInfo.append([lineRevised[0],listNums])

#print(springCondInfo)
    
#print(len(springCondInfo))

sumOfArrangements = 0



t0 = time.time()


for [springCondMap,orderedNums] in springCondInfo:

    sumOfArrange = 0
    
    binaryPlaces = springCondMap.count("?")

    maxIter = 2**binaryPlaces


    orderedNumsSum = sum(orderedNums)

    springCondMap = springCondMap.replace('#','1')
    springCondMap = springCondMap.replace('.','0')

    #PossiblePlaces = [index for index in range(len(springCondMap)) if springCondMap[index] == "?"]

    #print(PossiblePlaces)

    #binaryNumArray = [format(num,'0'+str(binaryPlaces)+'b') for num in range(maxIter)]

    #print(binaryNumArray)

    for binaryNum in range(maxIter):

        binaryNum = format(binaryNum,'0'+str(binaryPlaces)+'b')
        
        totalCounts = springCondMap.count('1') + binaryNum.count('1')
        
        if totalCounts != orderedNumsSum: continue
        
        
        #binaryNum = binaryNum.replace("0",'.')
        #binaryNum = binaryNum.replace("1",'#')
        
        springMapCopy = springCondMap

        for char in binaryNum:

            springMapCopy = springMapCopy.replace("?",char,1)

        #print(springMapCopy)

        #if springMapCopy.count('#') != orderedNumsSum: continue
               
        
        springMapCopy = springMapCopy.split('0')

        if len(springMapCopy)-springMapCopy.count('') != len(orderedNums): continue


        charLengths = [len(char) for char in springMapCopy if char != '']

        if charLengths == orderedNums:

            #print("match")

            sumOfArrange += 1
 
        #print(springMapCopy)

    #print(f"SpringcondCopy:{springCondMap}")

    #print(f"arrangement possible:{sumOfArrange}")

    sumOfArrangements += sumOfArrange

print(f"sum of total arrangements:{sumOfArrangements}")

print('{0:.50g}'.format(time.time()-t0))