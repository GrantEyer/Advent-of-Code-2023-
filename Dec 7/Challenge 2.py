#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

camelCards = []

camelCardsBids = []

for line in lines:

    line = line.split(' ')

    camelCards.append(line[0])

    camelCardsBids.append(int(line[-1]))

#print(camelCards)
#print(camelCardsBids)

characterList = ["A", "K", "Q", 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']

characterList = list(reversed(characterList))


camelCardTypes = list(reversed(["Five","Four","Full","Three","Two","One","High"]))

camelCardTypeInfo = {Type:[] for Type in camelCardTypes}



for camelCard in camelCards:

    charCountDict = {}

    

    for character in characterList[1:]:

        charCountDict[character] = camelCard.count(character)


        
    
    #print(camelCard)
    #print(charCountDict)

    count2Analyze = list(charCountDict.values())

    count2AnalyzeMax = max(count2Analyze)

    indexToAddTo = count2Analyze.index(count2AnalyzeMax)

    count2Analyze[indexToAddTo] += camelCard.count("J")


    if count2Analyze.count(5)==1:

        camelCardTypeInfo["Five"].append(camelCard)

    elif count2Analyze.count(4)==1:

        camelCardTypeInfo["Four"].append(camelCard)

    elif count2Analyze.count(3)==1 and count2Analyze.count(2)==1:

        camelCardTypeInfo['Full'].append(camelCard)

    elif count2Analyze.count(3)==1:

        camelCardTypeInfo['Three'].append(camelCard)

    elif count2Analyze.count(2) == 2:

        camelCardTypeInfo['Two'].append(camelCard)

    elif count2Analyze.count(2)==1:

        camelCardTypeInfo['One'].append(camelCard)

    else:
        camelCardTypeInfo['High'].append(camelCard)


cardsStrength = []

totalWinnings = 0

for cardType in camelCardTypes:

    #print(cardType)

    CamelCards = camelCardTypeInfo[cardType]
    
    
    if CamelCards:

        #print(camelCards)

        cardsReOrdered = {}

        for cards in CamelCards:

            valOfCard = list(cards)

            number = ''

            for val in valOfCard:

                #print(val)

                number += str((characterList.index(val)+10))

                #print(f"Number:{number}")



            cardsReOrdered[cards] = int(number)




        keyList = list(cardsReOrdered.keys())

        #print(f"KeyList:{keyList}")

        valuesList = list(cardsReOrdered.values())
 

        valuesSorted = sorted(valuesList)

        #print(f"Values sorted: {valuesSorted}")

        for value in valuesSorted:

            keyIndx = valuesList.index(value)

            hand = keyList[keyIndx]

            #print(hand)

            cardsStrength.append(hand)

            biddingIndx = camelCards.index(hand)

            #print(biddingIndx)

            bid = camelCardsBids[biddingIndx]

            #print(bid)
            #print(cardsStrength)

            totalWinnings += len(cardsStrength) * bid



        #print(cardsStrength)


#print(camelCardTypeInfo)
#print(len(characterList))
#print(len(cardsStrength))
print(totalWinnings)


 

        



