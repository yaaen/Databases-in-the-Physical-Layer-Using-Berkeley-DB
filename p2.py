from collections import Counter
import re

#Open the file and only have it so that it is being read.
f = open('10.txt', "r")
o = open('reviews.txt', "w")


#Read in the file line by line!
line  = True
counter = 1
counterChange = True
noCommaFlag = False



o.write(str(counter))
o.write(",")
#series of while loops that parse the input a metric ton.
while line:
    line = f.readline()
    line.strip('\n') 
    splittingFunction = line.split(": ",1)

    
    #PUT IN A " FOR THE SELECTED OPTION
    if (splittingFunction[0] == "review/text") or (splittingFunction[0] == "product/title") or(splittingFunction[0] == "review/summary") or (splittingFunction[0] == "review/profileName"):
        print("\"",end="")
        o.write("\"")




    print(splittingFunction[-1].strip('\n'),end="")
    o.write(splittingFunction[-1].strip('\n'))

    if line == "\n":
        print()
        o.write("\n")
        counter = counter +1
        print(counter,end="")
        o.write(str(counter))
        noCommaFlag = True


    if (splittingFunction[0] == "review/text"):
        continue

    if (splittingFunction[0] == "review/text") or (splittingFunction[0] == "product/title") or(splittingFunction[0] == "review/summary") or (splittingFunction[0] == "review/profileName"):
        print("\"",end="")
        o.write("\"")
    print(",", end="")

    #if (noCommaFlag != True):
    o.write(",")
    #    noCommaFlag = False
    #noCommaFlag = False
        

f.close()


#Part where I do all of the counting of all of the various words.
f2 = open('10.txt', "r")

numOccurances = {}

fileContents2 = f2.read()
file2Words = fileContents2.split(' ') #split by spaces
for word in file2Words:
    if word not in numOccurances:
        numOccurances[word] = 1
    else: 
        numOccurances[word] += 1

for (key,value) in numOccurances:
    print(key, value)







