import problem_2

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

# find number of commits for CDET
dict = find_branch_and_commit_id("CSCvv01962.txt")
num_commits = len(dict)
print("Number of commits:", num_commits)
print(dict)

# match branch names and build numbers for CDET
i = 0
for i in range(num_commits):
    new_value = list(dict)
    index_value = new_value[i]
    actual = dict.get(index_value)
    print(actual)
    problem_2.find_build_num("CSCvv01962",actual + "-prs.html")
    i += 1