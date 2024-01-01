#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

#find colon index for each line, then split the inout and extract all numbers
TimeOfRace = lines[0]


colonIndx = TimeOfRace.find(':')

TimeOfRace = TimeOfRace[colonIndx+1:]
TimeOfRace = TimeOfRace.split()

TotalTime = ''

for element in TimeOfRace: 

    if element != '': TotalTime += element

TotalTime = int(TotalTime)




RecordToBeat = lines[-1]

colonIndx = RecordToBeat.find(':')

RecordToBeat = RecordToBeat[colonIndx+1:]

RecordToBeat = RecordToBeat.split()

Record = ''

for element in RecordToBeat: 

    if element != '': Record += element

Record = int(Record)




waysToBeatRecord = 0

for buttonHoldTime in range(1,TotalTime):

    BoatSpeed = buttonHoldTime

    TimeRemaining = TotalTime - buttonHoldTime

    DistanceTraveled = TimeRemaining * BoatSpeed

    if DistanceTraveled > Record: waysToBeatRecord += 1

print(waysToBeatRecord)
