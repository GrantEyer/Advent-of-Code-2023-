#opens file that contains data
file = open('Challenge Input.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

totalSum = 0

for line in lines:

    line = line.split(' ')

    numArray = [int(num) for num in line if num != '']


    while any(numArray):


        for indx in range(len(numArray)-1):

            firstNum = numArray[indx+1]
            secondNum = numArray[indx]

            difference = firstNum-secondNum

            numArray[indx]=difference

        lastPrevNum = numArray.pop()

        totalSum += lastPrevNum

print(totalSum)



            

            




