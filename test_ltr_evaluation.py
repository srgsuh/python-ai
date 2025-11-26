import unittest as ut
from ltr_evaluation import eval

class testLtrEvaluation(ut.TestCase):
    def test_eval_success(self) -> None:
        self.assertAlmostEqual(5, eval("2 + 3"), 4)
        self.assertAlmostEqual(16, eval("3 + (2*10/(40 - 20))+ (3 * 4)"), 4)
        self.assertAlmostEqual(16, eval("3 + (2*10/(40 - 20))+ (3 * 4)"), 4)
        self.assertAlmostEqual(14, eval("10.0 + (10**2)/(20.5 + 4.25 + (25.0/100))"), 4)

if __name__ == "__main__":
    ut.main()