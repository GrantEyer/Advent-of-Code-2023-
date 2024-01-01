#opens file that contains data
file = open('Challenge 1.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

nums = []

for line in lines:
    numList=""
    for char in line:
      
        try:
            int(char)
        except ValueError: False
        else:
            numList += char

            numbers = list(numList)

        firstDigit = numbers[0]
        lastDigit = numbers[-1]

        num = firstDigit + lastDigit
            
    nums.append(int(num))

sum = sum(nums)
print(sum)

    
