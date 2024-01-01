#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')


seedLine = lines.pop(0)

colonIndx = seedLine.find(":")

seedNums = seedLine[colonIndx+1:].strip()

seedNums = seedNums.split(' ')

seedNums = [int(num) for num in seedNums if seedNums != '']



numberList = [str(num) for num in list(range(0,10))]


keyNums = seedNums

#print(seedNums)

Repeat = True

destList = []





for line in lines:

    #print(line)

    if line == '':
        destList = []
        continue

    elif line[0] in numberList:

        nums = line.split(' ')

        nums = [int(num) for num in nums if num != '']

        destStart = nums[0]

        sourceStart = nums[1]

        rangeLength = nums[-1]

        destRange = range(destStart,destStart+rangeLength)

        sourceRange = range(sourceStart,sourceStart+rangeLength)

        


        for elementIndx in range(0,len(keyNums)):

            element = keyNums[elementIndx]
            
            if element in sourceRange and elementIndx not in destList:
                   
                #print(element)
                

                destIndx = sourceRange.index(element)
                destMap = destRange[destIndx]

                destList.append(elementIndx)

                #print(destMap)

                keyNums[elementIndx] = destMap




    #print(keyNums) 


print(min(keyNums))

            

















