#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')


seedLine = lines.pop(0)

colonIndx = seedLine.find(":")

seedNumsRelated = seedLine[colonIndx+1:].strip()

seedNumsRelated = seedNumsRelated.split(' ')

seedNumRelated = [int(num) for num in seedNumsRelated if seedNumsRelated != '']

seedNums = []

numberList = [str(num) for num in list(range(0,10))]

locsList = []



for index in range(0,len(seedNumRelated)-1):

    seedNums = []

    if index % 2 == 0:
    
        SeedNumStart = seedNumRelated[index]
        SeedQuantity = seedNumRelated[index+1]

        seedNums = range(SeedNumStart,SeedNumStart+SeedQuantity)

        #print(seedNums)

        unconvertedRanges = [seedNums] 
        
        convertedRanges = []

        #print(lines)

        for lineIndx in range(0,len(lines)):

            line = lines[lineIndx]

            #print(line)



            if line == '':

                #print(f"Unconverted Ranges: {unconvertedRanges}")
                #print(f"Converted Ranges: {convertedRanges}")

                unconvertedRanges += convertedRanges
                convertedRanges = []
                   
                
                continue

            elif line[0] in numberList:

                nums = line.split(' ')

                nums = [int(num) for num in nums if num != '']

                destStart = nums[0]

                sourceStart = nums[1]

                rangeLength = nums[-1]

                destRange = range(destStart,destStart+rangeLength)

                sourceRange = range(sourceStart,sourceStart+rangeLength)

                startOfRange = -1

                startOfSourceRange = -1

                previousNum = -1

                inSourceRangeFlag = False

                unconvertedRangesNew = []

                #print(f"SourceRange: {sourceRange}")

                #print(f"Uncoverted: {unconvertedRanges}")

                for rangeElements in unconvertedRanges:

                    
                    #print(f"Range elements found {rangeElements}")

                    
                    startOfUnconvertedRange = rangeElements[0]

                    endOfUnconvertedRange = rangeElements[-1]


                    #if entire range is either the same as the source range or a subset of the range
                    if startOfUnconvertedRange in sourceRange and endOfUnconvertedRange in sourceRange:   
                        
                        #print("Branch 1")
                        
                        destMapStartIndx = sourceRange.index(startOfUnconvertedRange)
                        destMapEndIndx = sourceRange.index(endOfUnconvertedRange)

                        range2Add = range(destRange[destMapStartIndx],destRange[destMapEndIndx]+1)
                        
                        convertedRanges.append(range2Add)

                        #removalIndx = unconvertedRanges.index(rangeElements)

                        #unconvertedRanges.pop(removalIndx)

                        #print(f"Popped Range: {unconvertedRanges}")
 

                    #if the starting point of the enitre range is contained within the sourceRange, with some numbers on the right not being converted
                    elif startOfUnconvertedRange in sourceRange:

                        #print("Branch 2")
                        
                        destMapStartIndx = sourceRange.index(startOfUnconvertedRange)




                        destMapEndIndx = len(destRange)-1



                        range2Add = range(destRange[destMapStartIndx],destRange[destMapEndIndx]+1) 

                        convertedRanges.append(range2Add)



                        uncovertedRange2Add = range(sourceRange[-1]+1,endOfUnconvertedRange)
                        
                        unconvertedRangesNew.append(uncovertedRange2Add)

                        #removalIndx = unconvertedRanges.index(rangeElements)

                        #unconvertedRanges.pop(removalIndx)

                    #if there are numbers that come before sourceRange but sourceRange includes some elements until end of analyzed range
                    elif endOfUnconvertedRange in sourceRange:

                        #print("Branch 3")

                        destMapEndIndx = sourceRange.index(endOfUnconvertedRange)




                        destMapStartIndx = 0



                        range2Add = range(destRange[destMapStartIndx],destRange[destMapEndIndx]+1) 

                        convertedRanges.append(range2Add)



                        uncovertedRange2Add = range(startOfUnconvertedRange,sourceRange[0])
                        
                        unconvertedRangesNew.append(uncovertedRange2Add)

                        #removalIndx = unconvertedRanges.index(rangeElements)

                        #unconvertedRanges.pop(removalIndx)


                    #if source range is sandwhiched in between 
                    elif sourceStart in rangeElements and sourceRange[-1] in rangeElements:

                        #print("Branch 4")
                        
                        convertedRanges.append(destRange)

                        beforeUncovertedRange = range(startOfUnconvertedRange,sourceRange[0])

                        afterUncovertedRange = range(sourceRange[-1]+1,endOfUnconvertedRange)

                        unconvertedRangesNew.extend([beforeUncovertedRange,afterUncovertedRange])
                        

                    else:
                        
                        #print("Branch 5")

                        unconvertedRangesNew.append(rangeElements)


                
                
                    
                unconvertedRanges = unconvertedRangesNew

                    


                                


                        
        convertedRanges += unconvertedRanges
        #print(convertedRanges)
              
        locsList.extend(convertedRanges)


#print(locsList)

minIndexArr = []

for rangeNum in locsList:

    minIndexArr.append(rangeNum[0])

#print(minIndexArr)
print(min(minIndexArr))