from random import Random
from cols import Cols
from row import Row
from parse import parser
from utils import rnd

class Data:
    def __init__(self, src, nums, separator, randseed):
        self.cols = None
        self.rows = []
        self.n = nums
        self.rando = Random(randseed)
        def function(row):
            nonlocal self
            self.add(row)
        if isinstance(src, str):
            parser(src, function, separator)
        else:
            for row in (src or []):
                self.add(row)
    
    def add(self, xs):
        if self.cols == None:
            self.cols = Cols(xs)
        else:
            self.rows.append(xs if (hasattr(xs, 'cells')) else Row(xs))
            row = self.rows[-1]
            for todo in [self.cols.x, self.cols.y]:
                for col in todo:
                    col.add(row.cells[col.at], self.n, self.rando)

    def stats(self, places=2, show_cols="data.cols.x", fun = None):
        show_cols = show_cols or self.cols.y
        t= {}
        for col in show_cols:
            v = fun(col) if fun != None else col.mid()
            v = rnd(v, places) if isinstance(v, int) else v
            t[col.name] = v
        return t


















