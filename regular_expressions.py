def unsigned_float_number_pattern() -> str:
    """Define a pattern for the unsigned float number"""
    return r"(?:(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)"

def float_number_pattern() -> str:
    """Define a pattern for the signed float number"""
    ufn_format: str = unsigned_float_number_pattern()
    return rf"[+-]?{ufn_format}"

def arithmetic_operations_pattern() -> str:
    """"Define a pattern that matches any of the following arithmetic operations: +, -, /, * and **"""
    return r"(?:\+|\-|\*|/|\*\*)"

def ltr_no_parentheses_expr(num_pattern: str, op_pattern: str) -> str:
    """Define a pattern for the valid arithmetic expression that does not contain parentheses
    with binary operations defined in the `op_pattern` and numbers in the format defined by the `num_pattern`
    """
    return rf"(?:{num_pattern}{op_pattern})*{num_pattern}"