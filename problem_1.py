import re
#Regex pattern for cdets
pattern = re.compile("CSC[a-zA-Z][a-zA-Z]([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?")

#opening & reading in the branch, and split html file into list
file = open("v21.20.x-prs.html","r")
text = str(file.read()).split()

#should add user input here
build_1 = str(85903)
build_2 = str(85786)


b1_idx = 0
b2_idx = 0

try:
    #Locate where the build number is in the list
    b1_idx = text.index(build_1)
    b2_idx = text.index(build_2)
#if invalid build number is input
except ValueError:
    
    print("One or more build numbers are invalid.")


b1_end_idx = 0
b2_end_idx = 0
b1_cdets = []
b2_cdets = []



#interate from build number #1 index to end, break when five equal characters are found, as that indicates we are going past the current build number
for i in range(b1_idx + 2,len(text)):
    if text[i] == "=====":
        b1_end_idx = i
        break

#iterate from build number #1 index to the index found previously
for i in range(b1_idx+2,b1_end_idx):
    if bool(re.match(pattern,text[i])):
        b1_cdets.append(text[i])

#interate from build number #2 index to end, break when five equal characters are found, as that indicates we are going past the current build number
for i in range(b2_idx + 2,len(text)):
    if text[i] == "=====":
        b2_end_idx = i
        break

#iterate from build number #2 index to the index found previously
for i in range(b2_idx+2,b2_end_idx):
    if bool(re.match(pattern,text[i])):
        b2_cdets.append(text[i])

#find possible duplicate cdets. This will take care of scenario where user enters two same build numbers
duplicates = set(b1_cdets).intersection(b2_cdets)
isEmpty = (len(duplicates) == 0)

if isEmpty:
    print("No CDETs present between both builds.")
else:
    print(duplicates)




































