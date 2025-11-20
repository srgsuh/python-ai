def python_identifier_pattern() -> str:
    return r'[a-z_A-Z]\w*'

def pwd_pattern() -> str:
    return r"(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%])(?=.*[\d])[A-Za-z_#$%\d]{8,}"

def ipv4_pattern() -> str:
    #TODO
    raise NotImplementedError()

def israel_mobile_pattern() -> str:
    #TODO
    raise NotImplementedError()