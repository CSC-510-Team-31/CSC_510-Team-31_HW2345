import sys
import random
from constants import N_OPTION
from print import o

from sym import Sym
from utils import per


class Num(Sym):
  def __init__(self, c = 0, s = ""):
    super().__init__(c, s)
    self.n = 0
    self.at = c or 0
    self.name = s or ""
    self._has = []
    self.lo = sys.maxsize
    self.hi = -sys.maxsize
    self.isSorted = True
    self.w = -1 if (s or "").find("$") == -1 else 1
  
  def __repr__(self):
    return o({"at": self.at, "hi": self.hi, "isSorted": self.isSorted, "lo": self.lo, "n": self.n,
    "name": self.name, "w": self.w})

  def nums(self):
    if not self.isSorted: 
      self._has.sort()
      self.isSorted = True
    return self._has
    
  # v is a number -> value like key, value
  def add(self, v, nums, rand: random.Random):
    if v!="?":
      self.n = self.n +1
      self.lo = min(v, self.lo)
      self.hi = max(v, self.hi)

      if len(self._has) < nums:
        self.isSorted = False
        self._has.append(float(v))

      elif rand.random() < nums/self.n:
        # generate random int b/w 1, len of _has. As mentioned in csv.luna
        self.isSorted = False
        pos = rand.randint(0, len(self._has)-1)        
        self._has[pos] = float(v)
  
  def div(self):
    a = self.nums()
    return (per(a,.9) - per(a,0.1))/2.58

  def mid(self):
    return per(self.nums(),.5)







