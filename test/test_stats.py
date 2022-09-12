import test_type
from args import The
from constants import BIG_S_OPTION, F_OPTION, N_OPTION
from data import Data
from fileutils import read_file


class TestStats(test_type.TestType):
    def test_stats(self):
        temp_the = The()
        temp_the.the[F_OPTION] = "./data/small.csv"
        d = Data(read_file(temp_the), temp_the.the[N_OPTION], temp_the.the[BIG_S_OPTION])
        div = lambda thing: thing.div()
        mid = lambda thing: thing.mid()
        print("xmid", f"{d.stats(2,d.cols.x,mid)}")
        print("xdiv", f"{d.stats(3,d.cols.x,div)}")
        print("ymid", f"{d.stats(2,d.cols.y,mid)}")
        print("ydiv", f"{d.stats(3,d.cols.y,div)}")
        assert True
    
