from typing import Callable, Iterable
from regular_expressions import unsigned_float_number_pattern
import operator
import re

__operations: dict[str, Callable[[float, float], float]] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}

def iterable_pattern(iterable: Iterable) -> str:
    keys_str = "|".join([re.escape(k) for k in iterable])
    return rf"(?:{keys_str})"

__NUMBER_PATTERN: str = unsigned_float_number_pattern()
__OPERATION_PATTERN = iterable_pattern(__operations)

def __compute_one(op1: float, op2: float, operation_sign: str) -> float:
    operation_function = __operations.get(operation_sign)
    if operation_function is None:
        raise ValueError(f"Unsupported operation: {operation_sign}.")
    return operation_function(op1, op2)

def __eval_no_parentheses(expr: str) -> float:
    operands: list[str] = re.split(__OPERATION_PATTERN, expr)
    operations: list[str] = re.split(__NUMBER_PATTERN, expr)
    print(__NUMBER_PATTERN, __OPERATION_PATTERN)
    
    assert operands is not None and  operations is not None, "Illegal expression"
    res = float(operands[0])
    for i in range(1, len(operands)):
        res = __compute_one(res, float(operands[i]), operations[i])
    
    return res

def eval(expr: str) -> float:
    expr = re.sub(r"\s+", "", expr)
    while mo := re.search(r"\([^()]+\)", expr):
        inner = mo.group()[1:-1]
        value = __eval_no_parentheses(inner)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():]

    return __eval_no_parentheses(expr)