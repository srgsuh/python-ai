import unittest as ut
from regular_expressions import python_identifier_pattern, pwd_pattern, ipv4_pattern, israel_mobile_pattern
import re

class TestRegularExpressions(ut.TestCase):

    def test_python_identifier_pattern_true(self) -> None:
        self.assertTrue(re.fullmatch(python_identifier_pattern(), "__"))
        self.assertTrue(re.fullmatch(python_identifier_pattern(), "aAa12___"))
        self.assertTrue(re.fullmatch(python_identifier_pattern(), "test_python_identifier_pattern"))
        self.assertTrue(re.fullmatch(python_identifier_pattern(), "__a__"))

    def test_python_identifier_pattern_false(self) -> None:
        self.assertFalse(re.fullmatch(python_identifier_pattern(), "1__"))
        self.assertFalse(re.fullmatch(python_identifier_pattern(), "a b"))
        self.assertFalse(re.fullmatch(python_identifier_pattern(), "$a12b"))
        self.assertFalse(re.fullmatch(python_identifier_pattern(), "a*b"))

    def test_pwd_pattern_true(self) -> None:
        self.assertTrue(re.fullmatch(pwd_pattern(), "MNpq01#2"))
        self.assertTrue(re.fullmatch(pwd_pattern(), "__Az01$223145aff____"))
        self.assertTrue(re.fullmatch(pwd_pattern(), "__Az01_%_223145aff"))
        self.assertTrue(re.fullmatch(pwd_pattern(), "$#$#_1Gh$$$$$$$$$$$$$$$$"))

    def test_pwd_pattern_false(self) -> None:
        self.assertIsNone(re.fullmatch(pwd_pattern(), "MNpq0192")) # no special symbol
        self.assertIsNone(re.fullmatch(pwd_pattern(), "01232131232q#$")) # no Capital letter
        self.assertIsNone(re.fullmatch(pwd_pattern(), "MAIL_%_$#$")) # no lower-case letter
        self.assertIsNone(re.fullmatch(pwd_pattern(), "MnpQ_%_$#$")) # no digit
        self.assertIsNone(re.fullmatch(pwd_pattern(), "Mm#P123")) # Only 7 characters
        self.assertIsNone(re.fullmatch(pwd_pattern(), "MN(pq01#2")) # Contains forbidden symbol '('
        self.assertIsNone(re.fullmatch(pwd_pattern(), "")) # Empty string
    
    def test_ipV4_true(self) -> None:
        self.assertTrue(re.fullmatch(ipv4_pattern(), "0.0.0.0")) 
        self.assertTrue(re.fullmatch(ipv4_pattern(), "0.01.002.000")) 
        self.assertTrue(re.fullmatch(ipv4_pattern(), "000.1.249.59")) 
        self.assertTrue(re.fullmatch(ipv4_pattern(), "250.255.199.9"))
        self.assertTrue(re.fullmatch(ipv4_pattern(), "099.100.200.00"))
    
    def test_ipV4_false(self) -> None:
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0.0.0")) 
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0000.0.0.2"))  
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0.0.0.256"))
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0.0 0.2"))
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0.0.0.280"))
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0.0.0.0001"))
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0.0.0. 190"))
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0.0.0.+1"))
        self.assertFalse(re.fullmatch(ipv4_pattern(), "0.0.0.a"))
    
    def test_mobile_israel_true(self) -> None:
        self.assertTrue(re.fullmatch(israel_mobile_pattern(), "+972-54-1234567"))
        self.assertTrue(re.fullmatch(israel_mobile_pattern(), "+972-541234567")) 
        self.assertTrue(re.fullmatch(israel_mobile_pattern(), "+972-541234567"))
        self.assertTrue(re.fullmatch(israel_mobile_pattern(), "059123-45-67")) 
        self.assertTrue(re.fullmatch(israel_mobile_pattern(), "054-1-23-45-67"))
        self.assertTrue(re.fullmatch(israel_mobile_pattern(), "0571-23-45-67"))
    def test_mobile_israel_false(self) -> None:
        self.assertFalse(re.fullmatch(israel_mobile_pattern(), "+972-054-1234567"))
        self.assertFalse(re.fullmatch(israel_mobile_pattern(), "+972-54-1-234-567")) 
        self.assertFalse(re.fullmatch(israel_mobile_pattern(), "+972-54123456"))
        self.assertFalse(re.fullmatch(israel_mobile_pattern(), "059123-45-677")) 
        self.assertFalse(re.fullmatch(israel_mobile_pattern(), "054-1-2-3-45-67"))
        self.assertFalse(re.fullmatch(israel_mobile_pattern(), "0571-23-45-6-7"))
 
if __name__ == "__main__":
    ut.main()