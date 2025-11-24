import unittest as ut
from ltr_evaluation import eval

__delta = 1e-6

class testLtrEvaluation(ut.TestCase):
    def test_eval_01(self) -> None:
        self.assertAlmostEqual(5, eval("2 + 3"), 4)

    def test_eval_02(self) -> None:
        expr = "3 + (2*10/(40 - 20))+ (3 * 4)"
        self.assertEqual(16, eval(expr))
        self.assertAlmostEqual(16, eval(expr), 4)

if __name__ == "__main__":
    ut.main()