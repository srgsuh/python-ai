import regular_expressions as reg_expr
from utils import is_parentheses_pairing
from ltr_constants import blank_pattern, get_operation, ltr_pattern, inner_pattern, number_pattern, operation_pattern


def __is_valid_expression(expr: str) -> bool:
    return is_parentheses_pairing(expr) and (ltr_pattern.fullmatch(expr) is not None)

def __compute_one(op1: float, op2: float, operation_sign: str) -> float:
    operation_function = get_operation(operation_sign)
    return operation_function(op1, op2)

def __eval_no_parentheses(expr: str) -> float:
    operations: list[str] = number_pattern.split(expr)
    operands: list[str] = number_pattern.findall(expr) # fix to work with sci-format (e.g. 1e-2)

    res = float(operands[0])
    for i in range(1, len(operands)):
        res = __compute_one(res, float(operands[i]), operations[i])
    return res

def eval(expr: str) -> float:
    expr = blank_pattern.sub("", expr)
    if not __is_valid_expression(expr):
        raise ValueError(f"Invalid expression: {expr}")
    while mo := inner_pattern.search(expr):
        inner = mo.group()[1:-1]
        value = __eval_no_parentheses(inner)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():]

    return __eval_no_parentheses(expr)