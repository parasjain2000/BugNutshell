import re
pattern = re.compile("CSC[a-zA-Z][a-zA-Z]\d\d\d\d\d\s")

def find_cdets(build_1,build_2,file_name):
    b1_idx = 0
    b1_cdets = []
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

    if len(b1_cdets) == 0:
        return "One or more build numbers may be invalid"
    else:
        return b1_cdets


build_1 = 78834
build_2 = 78864
file_name = "v21.20.x-prs.html"

if build_1 > build_2:
    print(find_cdets(str(build_1),str(build_2),file_name))
else:
    print(find_cdets(str(build_2),str(build_1),file_name))
