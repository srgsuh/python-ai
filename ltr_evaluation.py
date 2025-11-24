import operator as op
import re

__operations: dict = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.floordiv,
    '**': op.pow
}

def __binCompute(op1: int, op2: int, operation: str) -> int:
    operator = __operations.get(operation)
    assert operator is not None, f"Operation {operation} not found"
    return operator(op1, op2)

def __eval_no_parentheses(expr: str) -> int:
    operands: list[str] = re.split(r"[/*+-]+", expr)
    operators: list[str] = re.split(r"\d+", expr)
    assert operands is not None and  operators is not None, "Illegal expression"
    res = int(operands[0])
    for i in range(1, len(operands)):
        res = __binCompute(res, int(operands[i]), operators[i])
    
    return res

def eval(expr: str) -> int:
    expr = re.sub(r"\s+", "", expr)
    while mo := re.search(r"\([^()]+\)", expr):
        inner = mo.group()[1:-1]
        value = __eval_no_parentheses(inner)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():]

    return __eval_no_parentheses(expr)