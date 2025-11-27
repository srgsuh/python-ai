import unittest as ut
import regular_expressions as regex
import re

class TestRegularExpressions(ut.TestCase):
    def setUp(self) -> None:
        self.signed_pattern: str = regex.float_number_pattern()
        self.unsigned_pattern: str = regex.unsigned_float_number_pattern()
        self.op_pattern: str = regex.arithmetic_operations_pattern()
        self.expr_pattern = regex.ltr_no_parentheses_expr(self.unsigned_pattern, self.op_pattern)
        self.full_expression: str = regex.ltr_expression(self.unsigned_pattern, self.op_pattern)
        self.full_pattern: re.Pattern = re.compile(self.full_expression)

    def test_float_number_true(self) -> None:
        float_pattern: str = self.signed_pattern
        self.assertTrue(re.fullmatch(float_pattern, "1.0"))
        self.assertTrue(re.fullmatch(float_pattern, ".0"))
        self.assertTrue(re.fullmatch(float_pattern, "0."))
        self.assertTrue(re.fullmatch(float_pattern, "100"))
        self.assertTrue(re.fullmatch(float_pattern, "-1e-6"))
        self.assertTrue(re.fullmatch(float_pattern, "6.02e-23"))
        self.assertTrue(re.fullmatch(float_pattern, ".271828e+1"))
        self.assertTrue(re.fullmatch(float_pattern, "+3.141592e0"))
    
    def test_float_number_false(self) -> None:
        float_pattern: str = self.signed_pattern
        self.assertIsNone(re.fullmatch(float_pattern, "."))
        self.assertIsNone(re.fullmatch(float_pattern, "+"))
        self.assertIsNone(re.fullmatch(float_pattern, "-"))
        self.assertIsNone(re.fullmatch(float_pattern, "1.0.0"))
        self.assertIsNone(re.fullmatch(float_pattern, "100e2e4"))
        self.assertIsNone(re.fullmatch(float_pattern, "e-2"))
        self.assertIsNone(re.fullmatch(float_pattern, "++0"))
        self.assertIsNone(re.fullmatch(float_pattern, "+-1"))
        self.assertIsNone(re.fullmatch(float_pattern, "1.1 01"))
        self.assertIsNone(re.fullmatch(float_pattern, "1..01"))
        self.assertIsNone(re.fullmatch(float_pattern, "1e-"))
    
    def test_unsigned_float_format_true(self) -> None:
        float_pattern: str = self.unsigned_pattern
        self.assertTrue(re.fullmatch(float_pattern, "0"))
        self.assertTrue(re.fullmatch(float_pattern, "1.0"))
        self.assertTrue(re.fullmatch(float_pattern, ".0"))
        self.assertTrue(re.fullmatch(float_pattern, "0."))
        self.assertTrue(re.fullmatch(float_pattern, "100"))
        self.assertTrue(re.fullmatch(float_pattern, "1e-4"))
        self.assertTrue(re.fullmatch(float_pattern, "6.022e-23"))
        self.assertTrue(re.fullmatch(float_pattern, ".271828e+1"))
        self.assertTrue(re.fullmatch(float_pattern, ".3141592e1"))
    
    def test_unsigned_float_number_false(self) -> None:
        float_pattern: str = self.unsigned_pattern
        self.assertIsNone(re.fullmatch(float_pattern, "."))
        self.assertIsNone(re.fullmatch(float_pattern, "+"))
        self.assertIsNone(re.fullmatch(float_pattern, "-"))
        self.assertIsNone(re.fullmatch(float_pattern, "1.0.0"))
        self.assertIsNone(re.fullmatch(float_pattern, "100e2e4"))
        self.assertIsNone(re.fullmatch(float_pattern, "e-2"))
        self.assertIsNone(re.fullmatch(float_pattern, "++0"))
        self.assertIsNone(re.fullmatch(float_pattern, "+-1"))
        self.assertIsNone(re.fullmatch(float_pattern, "1.1 01"))
        self.assertIsNone(re.fullmatch(float_pattern, "1..01"))
        self.assertIsNone(re.fullmatch(float_pattern, "1e-"))
        self.assertIsNone(re.fullmatch(float_pattern, "+3.141592e0"))
        self.assertIsNone(re.fullmatch(float_pattern, "-1e-6"))
        self.assertIsNone(re.fullmatch(float_pattern, "+1"))
        self.assertIsNone(re.fullmatch(float_pattern, "-10.25"))
    
    def test_arithmetic_operations_pattern_true(self) -> None:
        self.assertTrue(re.fullmatch(self.op_pattern, '+'))
        self.assertTrue(re.fullmatch(self.op_pattern, '-'))
        self.assertTrue(re.fullmatch(self.op_pattern, '/'))
        self.assertTrue(re.fullmatch(self.op_pattern, '*'))
        self.assertTrue(re.fullmatch(self.op_pattern, '**'))

    def test_arithmetic_operations_pattern_false(self) -> None:
        self.assertIsNone(re.fullmatch(self.op_pattern, '+-'))
        self.assertIsNone(re.fullmatch(self.op_pattern, '***'))
        self.assertIsNone(re.fullmatch(self.op_pattern, '1+'))
        self.assertIsNone(re.fullmatch(self.op_pattern, '//'))
    
    def test_arithmetic_expression_true(self) -> None:
        expr_pattern = self.expr_pattern
        
        self.assertTrue(re.fullmatch(expr_pattern, '1+1'))
        self.assertTrue(re.fullmatch(expr_pattern, '100-9'))
        self.assertTrue(re.fullmatch(expr_pattern, '100-1e-3'))
        self.assertTrue(re.fullmatch(expr_pattern, '2**10.0'))
        self.assertTrue(re.fullmatch(expr_pattern, '1-10.+1E+2**7.0'))

    def test_arithmetic_expression_false(self) -> None:
        expr_pattern = self.expr_pattern
        
        self.assertIsNone(re.fullmatch(expr_pattern, '(1+1)'))
        self.assertIsNone(re.fullmatch(expr_pattern, '100--9'))
        self.assertIsNone(re.fullmatch(expr_pattern, '100-1***2'))
        self.assertIsNone(re.fullmatch(expr_pattern, 'x+1'))
        self.assertIsNone(re.fullmatch(expr_pattern, '1//10.+1E+2**7.0'))
        self.assertIsNone(re.fullmatch(expr_pattern, '/2+1'))
        self.assertIsNone(re.fullmatch(expr_pattern, '/'))
        self.assertIsNone(re.fullmatch(expr_pattern, '1**'))

    def test_ltr_expression_true(self) -> None:
        pattern: re.Pattern = self.full_pattern
        
        self.assertTrue(pattern.fullmatch(".3141592e1"))
        self.assertTrue(pattern.fullmatch("((((1E+2))))"))
        self.assertTrue(pattern.fullmatch("(100)"))
        self.assertTrue(pattern.fullmatch("    1.0     "))
        self.assertTrue(pattern.fullmatch("  (  (  1.0     ))"))
        self.assertTrue(pattern.fullmatch("(     .3141592e1)"))
        self.assertTrue(pattern.fullmatch("(1+((2+((3-(4/(7**(2/1.0 *9.0**(8-(7/(2)))))))))-(8**2.0e1))/1.0)"))
        self.assertTrue(pattern.fullmatch("(  7+ 1.0/2.0)*((2.0)**(1-2e-1))"))
        self.assertTrue(pattern.fullmatch("(1+2.0-(3e+1-1+1-1+0))-1e-2-1e+1-(7)"))
        self.assertTrue(pattern.fullmatch("  (  ( (( 5 - 1 )   * (2-1))))"))
    
    def test_ltr_expression_false(self) -> None:
        pattern: re.Pattern = self.full_pattern
        self.assertFalse(pattern.fullmatch("*1"))
        self.assertFalse(pattern.fullmatch("3+"))
        self.assertFalse(pattern.fullmatch("1+/2"))
        self.assertFalse(pattern.fullmatch("(.3141592e1)()"))
        self.assertFalse(pattern.fullmatch("2 2 + 1"))
        self.assertFalse(pattern.fullmatch("22 + 1e -1"))
 
if __name__ == "__main__":
    ut.main()
