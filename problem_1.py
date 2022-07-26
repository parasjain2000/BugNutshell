import re
pattern = re.compile("CSC[a-zA-Z][a-zA-Z]\d\d\d\d\d\s")


#If a user inputs an invalid build number, the function will just return "No CDETs present between both builds."
def find_cdets(build_1,build_2,file_name):
    b1_idx = 0
    b2_idx = 0
    b1_cdets = []
    b2_cdets = []
    with open(file_name) as fp:
        if build_1 != build_2:
            for i, line in enumerate(fp):
                if build_1 in line:
                    b1_idx = i
                    break
            for i, line in enumerate(fp,start=b1_idx+1):
                mo = pattern.match(line)
                if mo != None:
                    b1_cdets.append(str(mo.group(0)).strip())
                if build_2 in line:
                    b2_idx = i
                    break
            for i, line in enumerate(fp,start=b2_idx+1):
                mo = pattern.match(line)
                if mo != None:
                    b2_cdets.append(str(mo.group(0)).strip())
                if "=====" in line:
                    break
        else:
            for i, line in enumerate(fp):
                if build_1 in line:
                    b1_idx = i
                    break
            for i, line in enumerate(fp,start=b1_idx+1):
                mo = pattern.match(line)
                if mo != None:
                    b1_cdets.append(str(mo.group(0)).strip())
                if "=====" in line:
                    break
    fp.close()

    duplicates = set(b1_cdets).intersection(b2_cdets)
    if build_1 == build_2:
        duplicates = b1_cdets
    isEmpty = (len(duplicates) == 0)
    if isEmpty:
        return "No CDETs present between both builds."
    else:
        return duplicates


#
print(find_cdets("85489","85188"))