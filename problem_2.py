def find_build_num(cdet, file_name):
  build= ""
  flag = False
  arr = []
  try:
    with open(file_name) as fp:
      for i, line in enumerate(fp):
        if "===== Build" in line:
          build = line.split(" ")[2]
        if cdet in line:
          flag = True
          arr.append(build)
    fp.close()
    if flag:
      return arr
    else:
      return "Invalid CDET"
  except:
    return "Invalid Branch"







