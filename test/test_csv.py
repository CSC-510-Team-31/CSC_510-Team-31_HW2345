from args import The
from constants import BIG_S_OPTION
from fileutils import read_file
from parse import parser
from print import oo
import test_type



class TestCsv(test_type.TestType):
    def test_csv(self):
        self.test_the = The()
        n = 0

        def inner_fun(row):
            nonlocal n
            n = n + 1
            if n <= 10:
                oo(row) 
        
        parser(read_file(self.test_the), inner_fun, self.test_the.the[BIG_S_OPTION] )
        assert True


        