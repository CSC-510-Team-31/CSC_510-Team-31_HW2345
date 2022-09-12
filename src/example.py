from random import Random
import traceback
from args import The
from constants import BIG_S_OPTION, D_OPTION, E_OPTION, F_OPTION, N_OPTION, SMALL_S_OPTION
from data import Data
from fileutils import read_file
from num import Num
from parse import parser
from print import oo
from sym import Sym

class Example(object):
    def run_examples(self, input_the):
        self.test_the = input_the
        self.rando = Random(input_the[SMALL_S_OPTION])
        failures = 0
        crashes = 0
        successes = 0
        methods = dir(self)
        test_methods = []
        test_opt = self.test_the[E_OPTION].lower()
        for method in methods:
            if method.startswith("eg_" + (test_opt if (test_opt != "all") else "")):
                test_methods.append(method)
        for test_method in test_methods:
            test_thing = getattr(self,test_method)
            print("Running " + test_method)
            try:
                test_thing()
                print("\033[92m {}\033[00m" .format("SUCCESS!!"))
                successes += 1
            except Exception as e:
                if self.test_the[D_OPTION] == True:
                    traceback.print_exc()
                if isinstance(e, AssertionError):
                    print("\033[91m {}\033[00m" .format("FAILED"))
                    failures += 1
                else:
                    print("\033[91m {}\033[00m" .format("CRASHED"))
                    crashes += 1
            print()
        return successes, failures
    
    def eg_num(self):
        num_test = Num()
        for each_num in range(1, 101):
            num_test.add(each_num, self.test_the[N_OPTION], self.rando)
        median, st_dev = num_test.mid(), num_test.div()

        oo({"mid": median, "div": st_dev})
        assert 50 <= median and median <= 52 and 30.5 < st_dev and st_dev < 32
    
    def eg_sym(self):
        sym_test = Sym(None, None)

        for letter in ["a", "a", "a", "a", "b", "b", "c"]:
            sym_test.add(letter)
        mode, entropy = sym_test.mid(), sym_test.div()
        entropy = entropy * 1000 // 1 / 1000
        oo({ "mid": mode, "div": entropy })
        assert mode == "a" and 1.37 <= entropy and entropy <= 1.38

    def eg_bignum(self):
        num_test = Num()
        bignum_the = The().the
        bignum_the[N_OPTION] = 32
        for i in range(1, 1001):
            num_test.add(i, bignum_the[N_OPTION], self.rando)

        oo(num_test.nums())
        assert 32 == len(num_test._has)

    def eg_the(self):
        self.params = The()
        oo(self.params.the)

    def eg_csv(self):
        csv_the = The().the
        csv_the[F_OPTION] = "./data/auto93.csv"
        n = 0
        def inner_fun(row):
            nonlocal n
            n = n + 1
            if n <= 10:
                oo(row) 
        parser(read_file(csv_the[F_OPTION]), inner_fun, csv_the[BIG_S_OPTION] )
        assert True
    
    def eg_data(self):
        data_the = The().the
        data_the[F_OPTION] = "./data/auto93.csv"
        d = Data(read_file(data_the[F_OPTION]), data_the[N_OPTION], data_the[BIG_S_OPTION], data_the[SMALL_S_OPTION])
        for col in d.cols.y:
            oo(col)
        assert True

    def eg_stats(self):
        data_the = The().the
        data_the[F_OPTION] = "./data/auto93.csv"
        d = Data(read_file(data_the[F_OPTION]), data_the[N_OPTION], data_the[BIG_S_OPTION], data_the[SMALL_S_OPTION])
        div = lambda thing: thing.div()
        mid = lambda thing: thing.mid()
        print("xmid", f"{d.stats(2,d.cols.x,mid)}")
        print("xdiv", f"{d.stats(3,d.cols.x,div)}")
        print("ymid", f"{d.stats(2,d.cols.y,mid)}")
        print("ydiv", f"{d.stats(3,d.cols.y,div)}")
        assert True

if __name__ == "__main__":
    testthe = The()
    testthe.the[E_OPTION] = "ALL"
    eg = Example().run_examples(testthe.the)