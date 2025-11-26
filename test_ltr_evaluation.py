import unittest as ut
from ltr_evaluation import eval

class testLtrEvaluation(ut.TestCase):
    def test_eval_success(self) -> None:
        self.assertAlmostEqual(5, eval("2 + 3"), 4)
        self.assertAlmostEqual(16, eval("3 + (2*10/(40 - 20))+ (3 * 4)"), 4)
        self.assertAlmostEqual(16, eval("3 + (2*10/(40 - 20))+ (3 * 4)"), 4)
        self.assertAlmostEqual(14, eval("10.0 + ((10**2)/(20.5 + 4.25 + (25.0/100)))"), 4)

    def test_eval_unpaired_parentheses(self) -> None:
        with self.assertRaises(ValueError):
            eval("(5 + 3) - ((7 + 1)")
        with self.assertRaises(ValueError):
            eval("(5 + 3) - (7 + 1))")
    
    def test_eval_wrong_parentheses_order(self) -> None:
        with self.assertRaises(ValueError):
            eval("(1+2))*((7+0)")
        with self.assertRaises(ValueError):
            eval(")1+2(")
    
    def test_eval_empty_parentheses(self) -> None:
        with self.assertRaises(ValueError):
            eval("(1+2)+()")
    
    def test_eval_wrong_token_order(self) -> None:
        with self.assertRaises(ValueError):
            eval("(1+2)+")
        with self.assertRaises(ValueError):
            eval("1/+2")
        with self.assertRaises(ValueError):
            eval("**(2 + 1)")
        with self.assertRaises(ValueError):
            eval("(2 + 1)/")
        with self.assertRaises(ValueError):
            eval("(2 + 1)//2")
        with self.assertRaises(ValueError):
            eval("(2 + 1)//2")
    
if __name__ == "__main__":
    ut.main()