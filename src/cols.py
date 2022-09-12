import re
from sym import Sym
from num import Num


class Cols:
    def __init__(self, names):
        self.names=names
        self.all=[]
        self.klass=None
        self.x=[]
        self.y=[]
        for c in range(0, len(names)):
            s = names[c]
            if re.search("[A-Z]+", s):
                self.all.append(Num(c, s))
            else:
                self.all.append(Sym(c, s))
            col = self.all[-1]
            if s.find(":") == -1:
                if s[-1] == '+' or s[-1] == '-':
                    self.y.append(col) 
                else:
                    self.x.append(col)
                
                if s[-1] == '$':
                    self.klass = col