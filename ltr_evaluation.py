from typing import Callable
import regular_expressions as reg_expr
from utils import is_parentheses_pairing
import operator
import re

__operations: dict[str, Callable[[float, float], float]] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}

__NUMBER_PATTERN: str = reg_expr.unsigned_float_number_pattern()
__OPERATION_PATTERN: str = reg_expr.iterable_items_pattern(__operations)
__EXPR_PATTERN: str = reg_expr.ltr_expression(__NUMBER_PATTERN, __OPERATION_PATTERN)

ltr_pattern: re.Pattern = re.compile(__EXPR_PATTERN)

def __is_valid_expression(expr: str) -> bool:
    return is_parentheses_pairing(expr) and (ltr_pattern.fullmatch(expr) is not None)

def __compute_one(op1: float, op2: float, operation_sign: str) -> float:
    operation_function = __operations.get(operation_sign)
    if operation_function is None:
        raise ValueError(f"Unsupported operation: {operation_sign}.")
    return operation_function(op1, op2)

def __eval_no_parentheses(expr: str) -> float:
    operands: list[str] = re.split(__OPERATION_PATTERN, expr)
    operations: list[str] = re.split(__NUMBER_PATTERN, expr)

    assert operands is not None and  operations is not None, "Illegal expression"
    res = float(operands[0])
    for i in range(1, len(operands)):
        res = __compute_one(res, float(operands[i]), operations[i])
    
    return res

def eval(expr: str) -> float:
    expr = re.sub(r"\s+", "", expr)
    if not __is_valid_expression(expr):
        raise ValueError(f"Invalid expression: {expr}")
    while mo := re.search(r"\([^()]+\)", expr):
        inner = mo.group()[1:-1]
        value = __eval_no_parentheses(inner)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():]

    return __eval_no_parentheses(expr)