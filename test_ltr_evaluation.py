import unittest as ut
from ltr_evaluation import eval

tol: int = 4

class testLtrEvaluation(ut.TestCase):
    def test_eval_success(self) -> None:
        self.assertAlmostEqual(1e-4, eval("1e-4"), places=tol)
        self.assertAlmostEqual(100, eval("((((1E+2))))"), places=tol)
        self.assertAlmostEqual(1, eval("5.000 +      5/1              /1e1"), places=tol)
        self.assertAlmostEqual(5, eval("2 + 3"), places=tol)
        self.assertAlmostEqual(16, eval("3**1.0 + (2*.1e+2/(40 - 20))+ (3*1E0 * 40.0*1e-1)"), places=tol)
        self.assertAlmostEqual(16, eval("3 + (2*10/(40 - 20))+ (3 * 4)"), places=tol)
        self.assertAlmostEqual(14, eval("10.0 + ((10**2)/(20.5 + 4.25 + (25.0/100)))"), places=tol)
        self.assertAlmostEqual(10, eval("4*1e+1/4.0"), places=tol)
        self.assertAlmostEqual(2.0*(2 - 3), eval("2.0*(2 - 3)"), places=tol)

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
            eval("(2 + 1)2")
    
    def test_eval_wrong_blank_placing(self) -> None:
        with self.assertRaises(ValueError):
            eval("2 2 + 1")
        with self.assertRaises(ValueError):
            eval("22 + 1e -1")
    
if __name__ == "__main__":
    ut.main()