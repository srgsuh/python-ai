import unittest as ut
from utils import is_parentheses_pairing

class TestUtils(ut.TestCase):
    def test_is_parentheses_pairing_true(self) -> None:
        self.assertTrue(is_parentheses_pairing("()()"))
        self.assertTrue(is_parentheses_pairing("()()((()()(())))"))
        self.assertTrue(is_parentheses_pairing("cos(sin(x))*(x + (2))/((x+y)-tan(x))"))
        self.assertTrue(is_parentheses_pairing("()((x - a)*(x + a))()"))
        self.assertTrue(is_parentheses_pairing("((((1E+2))))"))
    
    def test_is_parentheses_pairing_false(self) -> None:
        self.assertFalse(is_parentheses_pairing("("))
        self.assertFalse(is_parentheses_pairing("(1 + 3 - 4)("))
        self.assertFalse(is_parentheses_pairing(")"))
        self.assertFalse(is_parentheses_pairing("(2 + 3)**(7))"))
        self.assertFalse(is_parentheses_pairing("((7 + 8)/(2 - 11)"))
        self.assertFalse(is_parentheses_pairing("(1+2))*((7+0)"))

if __name__ == '__main__':
    ut.main()