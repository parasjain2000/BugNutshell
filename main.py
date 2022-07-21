stringCDET = input("CDET is: ")
stringdecimal = "Update version number for 21.20.36"
stringBeforeBuild = "===== Build"
stringAfterBuild = "Merged from other branches"
# opening a text file
file1 = open("v21.20.x-prs.html", "r")

  
# setting flag and index to 0
flag = 0
index = 0
  
# Loop through the file line by line
for line in file1:
  index += 1
  #splitting sentence to find branch
  if stringdecimal in line: 
    newstring = stringdecimal.partition("for ")
    y = newstring[2].partition(".")
    z = y[2].partition(".")
    branchnumber = y[0]+y[1]+z[0]
    print("Branch number is", branchnumber)
    
  # checking if CDET is present in line or not and printing line if present
  if stringCDET in line:
      flag = 1
      print('CDET', stringCDET, 'Found In Line', index)
  # checking condition for string not found and printing line
if flag == 0: 
   print('CDET', stringCDET , 'Not Found') 
  
# closing text file    
file1.close()
# opening a text file
file1 = open("v21.20.x-prs.html", "r")
#reading file
text = file1.read()
res = [i for i in range(len(text)) if text.startswith(stringBeforeBuild, i)]
# print("the start index is" + str(res))
mer = [i for i in range(len(text)) if text.startswith(stringAfterBuild, i)]
# print("the end index is" + str(mer))
# print(range(len(text)))
 
for i in range(len(res)):
  for j in range(len(mer)):
      par = text.find(stringCDET, res[i], mer[j])
      if(par) != -1:
        firstIdx = res[i]
        secondIdx = mer[j]
#fix hard code for 17 characters
        substring = text[firstIdx+len(stringBeforeBuild):firstIdx+17]
        print("Build Number is" + substring)
        break
      elif par == -1:
        print("Branch Not Found")
        break
  break
        
# closing text file
file1.close()
  
 