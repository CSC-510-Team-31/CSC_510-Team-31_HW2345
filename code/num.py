import sys
from sym import Sym


class Num(Sym):
  def __init__(self, c, s):
    super().__init__(c, s)
    self.lo = sys.maxsize
    self.hi = -sys.maxsize
    self.isSorted = True
    self.w = -1 if (s or "").find("$") == -1 else 1