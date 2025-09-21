# calculator.py
import ast
import operator as op
import math

ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
}

ALLOWED_FUNCS = {k: getattr(math, k) for k in dir(math) if not k.startswith('_')}
ALLOWED_NAMES = {'pi': math.pi, 'e': math.e}
ALLOWED_NAMES.update(ALLOWED_FUNCS)

def _eval(node):
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.Constant): # Py3.8+
        return node.value
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        return ALLOWED_OPERATORS[type(node.op)](operand)
    if isinstance(node, ast.Call):
        func = node.func.id
        if func in ALLOWED_NAMES:
            args = [_eval(a) for a in node.args]
            return ALLOWED_NAMES[func](*args)
        else:
            raise ValueError(f'Function {func} not allowed')
    if isinstance(node, ast.Name):
        if node.id in ALLOWED_NAMES:
            return ALLOWED_NAMES[node.id]
        else:
            raise ValueError(f'Name {node.id} is not allowed')
    raise TypeError(node)