import re

stringCDET = input("CDET is: ")
stringBeforeBuild = "===== Build"
stringAfterBuild = "Merged from other branches"
stringBeforeBranch = "Update version number for "
stringAfterBranch = "Merged"

#FINDING BRANCH NUMBER
# opening a text file
file1 = open("v21.20.x-prs.html", "r")
#reading file
text = file1.read()
#start index of stringBeforeBranch
resbranch = [
    i for i in range(len(text)) if text.startswith(stringBeforeBranch, i)
]
#start index of stringAfterBranch
merbranch = [
    i for i in range(len(text)) if text.startswith(stringAfterBranch, i)
]
#first occurence of "Update version number for branchnumber"
branchnum = text[resbranch[0]:merbranch[0]]
#partitioning code to find first four numbers
newstring = branchnum.partition("for ")
y = newstring[2].partition(".")
z = y[2].partition(".")
branchnumber = y[0] + y[1] + z[0]
#printing branch number
print("Branch number is " + branchnumber + ".x")
#closing a text file
file1.close()

#FINDING CDET
# opening a text file
file1 = open("v21.20.x-prs.html", "r")
# setting flag and index to 0
flag = 0
index = 0
# Loop through the file line by line
for line in file1:
    index += 1
    # checking if CDET is present in line or not and printing line if present
    if stringCDET in line:
        #CDET is present, tracks how many occurences
        flag += 1
        print('CDET', stringCDET, 'Found In Line', index)
    # checking condition for CDET not found and printing line
if flag == 0:
    print('CDET', stringCDET, 'Not Found')
# closing text file
file1.close()

#FINDING BUILD NUMBER
# opening a text file
file1 = open("v21.20.x-prs.html", "r")
#reading file
text = file1.read()
#start index of stringBeforeBuild
res = [i for i in range(len(text)) if text.startswith(stringBeforeBuild, i)]
#start index of stringAfterBuild
mer = [i for i in range(len(text)) if text.startswith(stringAfterBuild, i)]
#variable to track whether CDET found or not

for i in range(len(res)):
    for j in range(i, len(mer)):
        par = text.find(stringCDET, res[i], mer[j])
        #   if CDET is found in that paragraph
        if par != -1:
            #   change variable to reflect that the CDET is found, tracks how many times the CDET is found
            firstIdx = res[i]
            secondIdx = mer[j]
            #find index of stringBeforeBuild starting from par between res[i] and par
            buildIndex = text.rfind(stringBeforeBuild, res[i], par)

            if (firstIdx == buildIndex):
                #find stringAfterBuild starting from buildIndex
                endIndex = text.find(stringAfterBuild, buildIndex)
                #print paragraph
                substring = text[buildIndex:endIndex + len(stringAfterBuild)]
                print(substring)
        break
        if par == -1:
          print("Build Not Found")
# closing text file
file1.close()


