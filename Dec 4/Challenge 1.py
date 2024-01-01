#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

points = 0

for line in lines:

    colonIndx = line.find(":")
    delimeterIndx = line.find("|")




    WinningNumbers = line[colonIndx:delimeterIndx].strip()

    WinningNumbers = WinningNumbers.split(' ')

    WinningNumbers = [number for number in WinningNumbers if number!='']



    DrawnNumbers = line[delimeterIndx+1:].strip()

    DrawnNumbers = DrawnNumbers.split(' ')

    DrawnNumbers = [number for number in DrawnNumbers if number!='']


    matchedNums = [int(num) for num in DrawnNumbers if num in WinningNumbers]
    
    if matchedNums:
        points += 2**(len(matchedNums)-1)


print(points)





