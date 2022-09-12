import test_type
from data import Data
from print import oo
from args import The
from constants import BIG_S_OPTION, F_OPTION, N_OPTION
from fileutils import read_file

class TestData(test_type.TestType):
    def test_data(self):
        temp_the = The()
        temp_the.the[F_OPTION] = "./data/small.csv"
        d = Data(read_file(temp_the), temp_the.the[N_OPTION], temp_the.the[BIG_S_OPTION])
        for col in d.cols.y:
            oo(col)
        return True
