# 파이썬 SymPy의 expand, factor, Symbol 함수를 호출하고 기호변수 X를 선언합니다.
from sympy import expand, factor, Symbol

x = Symbol('x')

print(expand((x + 1) * (x + 5)))

print(factor(x**2 + 6*x + 5))
