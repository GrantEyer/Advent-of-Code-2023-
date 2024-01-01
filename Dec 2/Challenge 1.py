#opens file that contains data
file = open('Challenge 1.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')


sum = 0

colorDict = {"Red":12,"Green":13,"Blue":14}

targets = [12,13,14]

for line in lines:

    flag = ""

    colonLoc = line.find(":")

    games = line[colonLoc+1:].strip()

    games = games.split(";")


    for game in games:

        gameSplit = game.split(",")


        for component in gameSplit:

            component = component.strip().split(" ")


            numberOfCubes = int(component[0].strip())

            colorOfCubes = component[-1].title().strip()


            if colorDict[colorOfCubes] < numberOfCubes:
                flag = "Skip"
                
        if flag == "Skip": break


    if flag != "Skip":    

        lineBefore = line[0:colonLoc]

        lineBefore = lineBefore.split(" ")

        sum += int(lineBefore[-1].strip())

print(sum)



    