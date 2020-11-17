import json
from json import JSONEncoder

class word():
  def __init__(self, word, meaning):
    self.word = word
    self.meaning = meaning
    self.old = False 
    self.error = False

class verb():
  def __init__(self,w):
    self.infinitive = w.rstrip(" ")
    self.meaning = ''
    self.dictionary = []
    self.singular1st = ''
    self.singular2nd = ''
    self.singular3rd = ''
    self.plural1st = ''
    self.plural2nd = ''
    self.plural3rd = ''
    self.imperative = ''
    self.active = ''
    self.passive = ''
    self.adverbial = ''
    self.error = False 
    self.perfective = ''
    self.imperfective = ''
    self.kind = ''
  def tojson(self):
    return json.dumps(self, default=lambda o: o.__dict__)

class file():
  def __init__(self):
    self.namefile = ''
    self.number = 0
    self.separator = ''
    self.L = []
    self.script_dir = ""
    self.error = []
