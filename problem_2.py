
def find_build_num(cdet, file_name):
  l = ""
  flag = False

  try:
    with open(file_name) as fp:
      for i, line in enumerate(fp):
        if "===== Build" in line:
          l = line
        if cdet in line:
          flag = True
          break
    fp.close()
    if flag:
      return l.split(" ")[2]
    else:
      return "Invalid CDET"
  except:
    return "Invalid Branch"





