#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

matchesPerCard = dict()

for line in lines:

    

    colonIndx = line.find(":")
    spaceIndx = line.find(' ')
    delimeterIndx = line.find("|")


    


    WinningNumbers = line[colonIndx:delimeterIndx].strip()

    WinningNumbers = WinningNumbers.split(' ')

    WinningNumbers = [number for number in WinningNumbers if number!='']



    DrawnNumbers = line[delimeterIndx+1:].strip()

    DrawnNumbers = DrawnNumbers.split(' ')

    DrawnNumbers = [number for number in DrawnNumbers if number!='']


    matchedNums = [int(num) for num in DrawnNumbers if num in WinningNumbers]
    
    
    
    matchesPerCard[int(line[spaceIndx+1:colonIndx])] = len(matchedNums)


scratchCards = {cardNum:1 for cardNum in matchesPerCard.keys()}

for cardNum, matches in matchesPerCard.items():

   if matches:
       
    maxCardNum = matches + cardNum

    if maxCardNum > max(scratchCards.keys()): 
       
       maxCardNum = max(scratchCards.keys())

             
    rangeToAdd = range(cardNum+1,maxCardNum+1)



    for scratchAdd in rangeToAdd:
      #  print("In here")
      #  print(f"Cardnum: {cardNum}, scratchadded to card number {scratchAdd}")
        
        scratchCards[scratchAdd] += scratchCards[cardNum]
      #  print(scratchCards[scratchAdd])

        
#print(matchesPerCard)
#print(scratchCards)

totalScratchCards = 0

for numScratchCards in scratchCards.values(): totalScratchCards += numScratchCards

print(totalScratchCards)