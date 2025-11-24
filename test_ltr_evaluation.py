import unittest as ut
from ltr_evaluation import eval

class testLtrEvaluation(ut.TestCase):
    def test_eval_01(self):
        self.assertEqual(5, eval("2 + 3"))

    def test_eval_02(self):
        expr = "3 + (2*10/(40 - 20))+ (3 * 4)"
        self.assertEqual(16, eval(expr))

if __name__ == "__main__":
    ut.main()