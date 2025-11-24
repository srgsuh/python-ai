def python_identifier_pattern() -> str:
    return r'[a-z_A-Z]\w*'

def pwd_pattern() -> str:
    return r"(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%])(?=.*[\d])[A-Za-z_#$%\d]{8,}"

def ipv4_pattern() -> str:
    """returns regexp as match pattern of IPv4 address
       comprises of 4 octets separated by dot
       each octet contains 1-3 symbols from 0 to 255
    """
    return  r"(([0-1]?\d{1,2}|25[0-5]|2[0-4][0-9])\.){3}([0-1]?\d{1,2}|25[0-5]|2[0-4][0-9])"

def israel_mobile_pattern() -> str:
    """returns regexp for mobile phone Israel number
       +972- - Israel preffix (not mandatary)
       Operator preffix 0 (only without +972-)
       50,51, 52, 53, 54, 55, 56, 57,58, 59
       optional dash
       7 digits as follows
       xxxxxxx
       xxx-xx-xx
       x-xx-xx-xx
    """
    
    return r"(\+972-|0)5\d-?(\d{7}|(\d-?\d{2}-\d{2}-\d{2}))"

def float_number_pattern() -> str:
    return r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?"