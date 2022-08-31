class Sym:
  def __init__(self, c, s):
    self.n = 0,
    self.at = c or 0
    self.name = s or ""
    self._has = {}