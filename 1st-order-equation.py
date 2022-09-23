# SymPy 라이브러리를 불러오고, 사용할 기호 변수 x를 선업합니다.
from sympy import Symbol, solve
x = Symbol('x')

# 방정식을 풀려면 "(일차방정식) = 0"으로 만들어 주어야 합니다.
# 이를 위해 모든 식을 좌변으로 이한한 후 equation으로 변수화합니다.
equation = 2 * x - 6

# 방정식을 풀려면 SymPy에 내장된 solve() 함수를 사용합니다.
# solve() 함수 안에 equation을 입력하면
# 방정식을 풀어서 결과를 반환합니다.
print(solve(equation))
