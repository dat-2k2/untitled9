from numpy import random
import numpy as np
from google.colab import files
import os
import urllib
import pandas as pd

class conjugate():
  def prepare(x):
    if (len(x) > 0):
      t = ''
      for i in range (0, len(x)):
        if ord(x[i]) in range (1040,1106):
          t = t + x[i]
      return t
    else: return ''
  def prepare2(x):
    if (len(x) > 0):
      t = ''
      for i in range (0, len(x)):
        if ord(x[i]) in range (65,91) or ord(x[i]) in range (97,123):
          t = t + x[i]
      return t
    else: return ''

  def conjugate(self):
    webpage = "http://en.wiktionary.org/wiki/"
    link = urllib.parse.quote(self.infinitive)
    webpage = urllib.parse.urljoin(webpage, link)
    try:
      urllib.request.urlopen(webpage)
    except urllib.error.HTTPError:
      self.error = True
    if self.error == False:
      span = pd.read_html(webpage)
      d = []
      for x in span:
        d.append(x.to_dict())
      check = 2
      temp = {}
      for x in d: 
        if 'imperfective aspect.1' in x.keys(): 
          temp = x
          check = 0
          break
        if 'perfective aspect.1' in x.keys():
          temp = x
          check = 1
          break
      l = []
      if check == 0 :
        self.active = conjugate.prepare(temp['imperfective aspect.1'][2])
        self.passive = conjugate.prepare(temp['imperfective aspect.1'][3])
        self.adverbial = conjugate.prepare(temp['imperfective aspect.1'][4])
        self.singular1st = conjugate.prepare(temp['imperfective aspect.1'][6])
        self.singular2nd = conjugate.prepare(temp['imperfective aspect.1'][7])
        self.singular3rd = conjugate.prepare(temp['imperfective aspect.1'][8])
        self.plural1st = conjugate.prepare(temp['imperfective aspect.1'][9])
        self.plural2nd = conjugate.prepare(temp['imperfective aspect.1'][10])
        self.plural3rd = conjugate.prepare(temp['imperfective aspect.1'][11])
        self.imperative = conjugate.prepare(temp['imperfective aspect.1'][13])
      elif check == 1:
        self.active = conjugate.prepare(temp['perfective aspect.2'][2])
        self.passive = conjugate.prepare(temp['perfective aspect.2'][3])
        self.adverbial = conjugate.prepare(temp['perfective aspect.2'][4])
        self.singular1st = conjugate.prepare(temp['perfective aspect.2'][6])
        self.singular2nd = conjugate.prepare(temp['perfective aspect.2'][7])
        self.singular3rd = conjugate.prepare(temp['perfective aspect.2'][8])
        self.plural1st = conjugate.prepare(temp['perfective aspect.2'][9])
        self.plural2nd = conjugate.prepare(temp['perfective aspect.2'][10])
        self.plural3rd = conjugate.prepare(temp['perfective aspect.2'][11])
        self.imperative = conjugate.prepare(temp['perfective aspect.1'][13])
      else: self.error = True


class main():
  def reverse_card(self):
    l = len(self.L)
    reverse = file()
    reverse.namefile = self.namefile + "[:-1]"
    reverse.separator = self.separator
    file2 = open(reverse.namefile, 'w')
    for x in self.L:
      t = x.meaning.rstrip("\n") + reverse.separator + x.word.rstrip("\n")
      file2.writelines(t)
      file2.writelines("\n")
      temp = word(x.meaning,x.word)
      reverse.L.append(temp)
    file2.close()
    return reverse 
  def writing_meaning(self):
    self.number = int(input("How many tasks would you want?"))
    Lines = []
    for x in self.L:
      Lines.append(x.word)
    l = len(self.L)
    arr = []
    for x in range (0,l):
      arr.append(x)
    arr = np.array(arr)
    need = []
    for x in range (0,self.number):
      name = str(x) + '.txt'
      abs_file_path = os.path.join(self.script_dir,name)
      filet = open(abs_file_path, 'w')
      temp  = random.permutation(arr)
      res = []
      count = True 
      for x in temp: 
        if (count == True): 
          filet.write(Lines[x].rstrip("\n"))
          filet.write("                            ".rstrip("\n"))
          count = not count
        else:
          filet.write(Lines[x]+"                    ")
          filet.write("\n")
          filet.write("\n")
          count = not count    
      filet.close()
  def solution(self):
    name = str(self.namefile) + "_sol.txt" 
    path = os.path.join(self.script_dir,name)
    f = open(path,'w')
    for x in self.L:
      f.writelines(x.word.rstrip("\n") + ": " + x.meaning)
      f.writelines("\n")
    f.close()
  def conjugate(self):
    y = verb(conjugate.prepare(self))
    conjugate.conjugate(y)
    if y.error == False:
     d = {'1st': [y.singular1st, y.plural1st], '2nd': [y.singular2nd, y.plural2nd], '3rd': [y.singular3rd, y.plural3rd] }
     df = pd.DataFrame.from_dict(data=d, orient = 'index', columns = ['singular','plural'])
     print(df)
    else: print("This word is not a Russian verb, or mistyped")
  def check(self):
    webpage = "http://en.wiktionary.org/wiki/"
    link = urllib.parse.quote(conjugate.prepare(self.word))
    webpage = urllib.parse.urljoin(webpage, link)
    try:
      urllib.request.urlopen(webpage)
    except urllib.error.HTTPError:
      self.error = True

