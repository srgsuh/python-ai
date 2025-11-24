import unittest as ut
import regular_expressions as regex
import re

class TestRegularExpressions(ut.TestCase):

    def test_python_identifier_pattern_true(self) -> None:
        pi_pattern = regex.python_identifier_pattern()
        self.assertTrue(re.fullmatch(pi_pattern, "__"))
        self.assertTrue(re.fullmatch(pi_pattern, "aAa12___"))
        self.assertTrue(re.fullmatch(pi_pattern, "test_python_identifier_pattern"))
        self.assertTrue(re.fullmatch(pi_pattern, "__a__"))

    def test_python_identifier_pattern_false(self) -> None:
        pi_pattern = regex.python_identifier_pattern()
        self.assertFalse(re.fullmatch(pi_pattern, "1__"))
        self.assertFalse(re.fullmatch(pi_pattern, "a b"))
        self.assertFalse(re.fullmatch(pi_pattern, "$a12b"))
        self.assertFalse(re.fullmatch(pi_pattern, "a*b"))

    def test_pwd_pattern_true(self) -> None:
        self.assertTrue(re.fullmatch(regex.pwd_pattern(), "MNpq01#2"))
        self.assertTrue(re.fullmatch(regex.pwd_pattern(), "__Az01$223145aff____"))
        self.assertTrue(re.fullmatch(regex.pwd_pattern(), "__Az01_%_223145aff"))
        self.assertTrue(re.fullmatch(regex.pwd_pattern(), "$#$#_1Gh$$$$$$$$$$$$$$$$"))

    def test_pwd_pattern_false(self) -> None:
        self.assertIsNone(re.fullmatch(regex.pwd_pattern(), "MNpq0192")) # no special symbol
        self.assertIsNone(re.fullmatch(regex.pwd_pattern(), "01232131232q#$")) # no Capital letter
        self.assertIsNone(re.fullmatch(regex.pwd_pattern(), "MAIL_%_$#$")) # no lower-case letter
        self.assertIsNone(re.fullmatch(regex.pwd_pattern(), "MnpQ_%_$#$")) # no digit
        self.assertIsNone(re.fullmatch(regex.pwd_pattern(), "Mm#P123")) # Only 7 characters
        self.assertIsNone(re.fullmatch(regex.pwd_pattern(), "MN(pq01#2")) # Contains forbidden symbol '('
        self.assertIsNone(re.fullmatch(regex.pwd_pattern(), "")) # Empty string
    
    def test_ipV4_true(self) -> None:
        self.assertTrue(re.fullmatch(regex.ipv4_pattern(), "0.0.0.0")) 
        self.assertTrue(re.fullmatch(regex.ipv4_pattern(), "0.01.002.000")) 
        self.assertTrue(re.fullmatch(regex.ipv4_pattern(), "000.1.249.59")) 
        self.assertTrue(re.fullmatch(regex.ipv4_pattern(), "250.255.199.9"))
        self.assertTrue(re.fullmatch(regex.ipv4_pattern(), "099.100.200.00"))
    
    def test_ipV4_false(self) -> None:
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0.0.0")) 
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0000.0.0.2"))  
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0.0.0.256"))
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0.0 0.2"))
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0.0.0.280"))
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0.0.0.0001"))
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0.0.0. 190"))
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0.0.0.+1"))
        self.assertFalse(re.fullmatch(regex.ipv4_pattern(), "0.0.0.a"))
    
    def test_mobile_israel_true(self) -> None:
        im_pattern: str = regex.israel_mobile_pattern()
        self.assertTrue(re.fullmatch(im_pattern, "+972-54-1234567"))
        self.assertTrue(re.fullmatch(im_pattern, "+972-541234567")) 
        self.assertTrue(re.fullmatch(im_pattern, "+972-541234567"))
        self.assertTrue(re.fullmatch(im_pattern, "059123-45-67")) 
        self.assertTrue(re.fullmatch(im_pattern, "054-1-23-45-67"))
        self.assertTrue(re.fullmatch(im_pattern, "0571-23-45-67"))

        self.assertTrue(re.fullmatch(im_pattern, "057-123-45-67"))
        self.assertTrue(re.fullmatch(im_pattern, "057123-45-67"))

    
    def test_mobile_israel_false(self) -> None:
        im_pattern: str = regex.israel_mobile_pattern()
        self.assertFalse(re.fullmatch(im_pattern, "+972-054-1234567"))
        self.assertFalse(re.fullmatch(im_pattern, "+972-54-1-234-567")) 
        self.assertFalse(re.fullmatch(im_pattern, "+972-54123456"))
        self.assertFalse(re.fullmatch(im_pattern, "059123-45-677")) 
        self.assertFalse(re.fullmatch(im_pattern, "054-1-2-3-45-67"))
        self.assertFalse(re.fullmatch(im_pattern, "0571-23-45-6-7"))

        self.assertFalse(re.fullmatch(im_pattern, "+972-5123-45-67"))
        self.assertFalse(re.fullmatch(im_pattern, "05123-45-67"))
        self.assertFalse(re.fullmatch(im_pattern, "05123-45-67"))
        self.assertFalse(re.fullmatch(im_pattern, "050--1-22-22-22"))
        self.assertFalse(re.fullmatch(im_pattern, "067-123-45-67"))
        self.assertFalse(re.fullmatch(im_pattern, "05a-123-45-67"))
        self.assertFalse(re.fullmatch(im_pattern, "+972541234567"))
        self.assertFalse(re.fullmatch(im_pattern, "+972-44-1234567"))
    
    def test_float_number_true(self) -> None:
        float_pattern: str = regex.float_number_pattern()
        self.assertTrue(re.fullmatch(float_pattern, "1.0"))
        self.assertTrue(re.fullmatch(float_pattern, ".0"))
        self.assertTrue(re.fullmatch(float_pattern, "0."))
        self.assertTrue(re.fullmatch(float_pattern, "100"))
        self.assertTrue(re.fullmatch(float_pattern, "-1e-6"))
        self.assertTrue(re.fullmatch(float_pattern, "6.02e-23"))
        self.assertTrue(re.fullmatch(float_pattern, ".271828e+1"))
        self.assertTrue(re.fullmatch(float_pattern, "+3.141592e0"))
    
    def test_float_number_false(self) -> None:
        float_pattern: str = regex.float_number_pattern()
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
        float_pattern: str = regex.unsigned_float_number_pattern()
        self.assertTrue(re.fullmatch(float_pattern, "1.0"))
        self.assertTrue(re.fullmatch(float_pattern, ".0"))
        self.assertTrue(re.fullmatch(float_pattern, "0."))
        self.assertTrue(re.fullmatch(float_pattern, "100"))
        self.assertTrue(re.fullmatch(float_pattern, "6.02e-23"))
        self.assertTrue(re.fullmatch(float_pattern, ".271828e+1"))
    
    def test_unsigned_float_number_false(self) -> None:
        float_pattern: str = regex.unsigned_float_number_pattern()
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
 
if __name__ == "__main__":
    ut.main()