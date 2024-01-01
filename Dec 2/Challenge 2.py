from functools import reduce

#opens file that contains data
file = open('Challenge 1.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')


sum = 0


for line in lines:


    colorDict = {"Red":0,"Green":0,"Blue":0}

    colonLoc = line.find(":")

    games = line[colonLoc+1:].strip()

    games = games.split(";")


    for game in games:

        gameSplit = game.split(",")


        for component in gameSplit:

            component = component.strip().split(" ")

            numberOfCubes = int(component[0].strip())

            colorOfCubes = component[-1].title().strip()

            if colorDict[colorOfCubes] == 0:
                colorDict[colorOfCubes] = numberOfCubes

            elif colorDict[colorOfCubes] < numberOfCubes:
                colorDict[colorOfCubes] = numberOfCubes

        
    sum += reduce(lambda x,y: x*y, list(colorDict.values()))


print(sum)



    