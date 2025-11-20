def python_identifier_pattern() -> str:
    return r'[a-z_A-Z]\w*'

def pwd_pattern() -> str:
    return r"(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%])(?=.*[\d])[A-Za-z_#$%\d]{8,}"

def ipv4_pattern() -> str:
    return  r"(([0-1]?\d{1,2}|25[0-5]|2[0-4][0-9])\.){3}([0-1]?\d{1,2}|25[0-5]|2[0-4][0-9])"

def israel_mobile_pattern() -> str:
    #TODO
    raise NotImplementedError()