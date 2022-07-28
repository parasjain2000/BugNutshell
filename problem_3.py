
def find_branch_and_commit_id(file_name):
    dict = {}
    #commit id: branch
    with open (file_name) as fp:
        for i, line in enumerate(fp):
            if "CSCvv" in line and "boxer" in line and "mergedtobranch" in line:
                title = line.split(" ")[0]
                title_s = title.split(".")
                dots = title.count('.')
                commit_id = title_s[dots].replace("ascii","")
                branch = title_s[3]
                hi = title_s[dots-1]
                for i in range(4,dots):
                    branch = branch + "." + title_s[i]

                dict[commit_id] = branch
    fp.close()
    return dict


dict = find_branch_and_commit_id("CSCvv01962.txt")
print(dict)




