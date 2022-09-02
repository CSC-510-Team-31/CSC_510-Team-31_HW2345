import math


class Sym:
  def __init__(self, c, s):
    self.n = 0
    self.at = c or 0
    self.name = s or ""
    self._has = {}
  
  def add(self, v):
    if v == "?":
      return
    self.n += 1
    self._has[v] = 1 + (self._has[v] if v in self._has else 0)
  
  def mid(self):
    most = -1
    for k, v in self._has.items():
      if v > most:
        mode, most = k, v
    return mode
  
  def div(self):
    def fun(p):
      return p * math.log(p, 2)
    e = 0
    for n in self._has.values():
      if n > 0:
        e -= fun(n / self.n)
    return e
