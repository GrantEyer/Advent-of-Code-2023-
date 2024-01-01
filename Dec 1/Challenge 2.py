#opens file that contains data
file = open('Challenge 1.txt','r')

#reads the file and splits lines by finding the blank lines
lines = file.read()
lines = lines.split('\n')

nums = []

for line in lines:
    
    line = line.lower()

    firstDigit = ""
    minIndex=len(line)

    lastDigit = ""
    maxIndex = 0

    wordNums = ["one","two","three","four","five","six","seven","eight","nine"]
    Nums =  ["1","2","3","4","5","6","7","8","9"] 

    Nums.extend(wordNums)

    for i in range(len(Nums)):
        if Nums[i] in line:
           NumIndicies = [index for index in range(len(line)) if line.startswith(Nums[i],index)]
            
           if min(NumIndicies) <= minIndex:
               
               minIndex=min(NumIndicies)
               if Nums[i] in wordNums:
                
                   firstDigit = str(wordNums.index(Nums[i])+1)
               else:
                   firstDigit = Nums[i]

           if max(NumIndicies)>= maxIndex:
                maxIndex=max(NumIndicies)
                
                if Nums[i] in wordNums:
                   lastDigit = str(wordNums.index(Nums[i])+1)
                else:
                   lastDigit = Nums[i]

  
    num = firstDigit + lastDigit    
            
    nums.append(int(num))

sum = sum(nums)
print(sum)