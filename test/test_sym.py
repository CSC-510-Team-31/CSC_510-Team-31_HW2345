from sym import Sym
from print import oo

class TestSym():
    def test_sym(self):
        self.sym_test = Sym(None, None)

        for letter in ["a", "a", "a", "a", "b", "b", "c"]:
            self.sym_test.add(letter)
        mode, entropy = self.sym_test.mid(), self.sym_test.div()
        entropy = entropy * 1000 // 1 / 1000
        oo({ "mid": mode, "div": entropy })
        assert mode == "a" and 1.37 <= entropy and entropy <= 1.38

