#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

#find colon index for each line, then split the inout and extract all numbers
TimeOfRaces = lines[0]


colonIndx = TimeOfRaces.find(':')

TimeOfRaces = TimeOfRaces[colonIndx+1:]
TimeOfRaces = TimeOfRaces.split()

TimeOfRaces = [int(num) for num in TimeOfRaces if num != '']


RecordsToBeat = lines[-1]


colonIndx = RecordsToBeat.find(':')

RecordsToBeat = RecordsToBeat[colonIndx+1:]
RecordsToBeat = RecordsToBeat.split()

RecordsToBeat = [int(num) for num in RecordsToBeat if num != '']

TimeDistanceRecord = {TimeOfRaces[i]:RecordsToBeat[i] for i in range(len(TimeOfRaces))}

waysToBeatRecords = 1


for Time, Record in TimeDistanceRecord.items():

    waysToWin = 0

    for buttonHoldTime in range(Time):

        BoatSpeed = buttonHoldTime

        TimeRemaining = Time - buttonHoldTime

        DistanceTraveled = TimeRemaining * BoatSpeed

        if DistanceTraveled > Record: waysToWin += 1

    
    waysToBeatRecords *= waysToWin

print(waysToBeatRecords)
