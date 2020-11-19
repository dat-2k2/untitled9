import os 

class INPUT():
  def INP(self):
    self.separator = input("Enter the sepаrator: ")
    self.namefile = input("Enter the input file: ")
    # when using the input() method, variable must have been initialized before
    try:
      filea = open(self.namefile, 'r')
    except FileNotFoundError:
      filea = open(self.namefile,'w+') 
    print("PLEASE CHARGE THE DATA, TYPE 'Y' WHEN YOU'VE DONE")
    x = ''
    x = input()
    if x != 'Y' and x != 'y':
      raise NotDone(x)
    а = 0
    if os.path.getsize(self.namefile) == 0:
      raise Empty(self.namefile)
    filea.close()
  def setup(self):
    d = "/content/"
    s = self.namefile + "_tasks"
    self.script_dir = os.path.join(d,s)
    os.mkdir(self.script_dir)
    f = open(self.namefile, 'r')
    Lines = f.readlines()
    for x in Lines:
      n = len(x)
      string1 = ''
      i = 0
      while i < n:
        if x[i] != self.separator:
          string1 = string1 + x[i]
          i = i + 1
        else: break
      string2 = ''
      while i < n:
        if x[i] != self.separator:
          string2 = string2 + x[i]
        i = i + 1
      x = word(string1, string2)
      self.L.append(x)
    f.close()
  def anki_input(self):
      f = open(self.namefile, 'r')
      x = f.readlines()
      self.L = []
      direct = open(self.namefile + ".json", 'a+')
      for line in x:
        temp = line.split("\t")
        temp1 = verb(temp[1])
        temp1.meaning = temp[2]
        temp1.kind = temp[3]
        temp1.imperfective = temp[4]
        temp1.perfective = temp[5]
        conjugate.conjugate(temp1)
        self.L.append(temp1) #must parse to JSON serializable 
        json.dump(temp1.tojson(), direct)



