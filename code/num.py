import sys
import math, random

from sym import Sym
from utils import per


class Num(Sym):
  def __init__(self, c, s):
    super().__init__(c, s)
    self.n = 0
    self.at = c or 0
    self.name = s or ""
    self._has = {}
    self.lo = sys.maxsize
    self.hi = -sys.maxsize
    self.isSorted = True
    self.w = -1 if (s or "").find("$") == -1 else 1

  def nums(self):
    if not self.isSorted: 
      self._has.sort()
      self.isSorted = True
    return self._has
    
  # v is a number -> value like key, value
  def add(self, v, the):
    if v!="?":
      self.n = self.n +1
      self.lo = min(v, self.lo)
      self.hi = max(v,self.hi)

      if len(self._has) < the.nums/self.n:
        pos = 1 + len(self.has)

      elif random.random() < the.nums/self.n:
        # generate random int b/w 1, len of _has. As mentioned in csv.luna
        pos = random.randint(1, len(self._has))

      if pos:
        self.isSorted = False
        self._has[pos] = float(v)
  
  def div(self):
    a = self.nums()
    return (per(a,.9) - per(a,0.1))/2.58





if __name__=="__main__":
  num = Num()







