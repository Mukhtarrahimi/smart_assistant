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