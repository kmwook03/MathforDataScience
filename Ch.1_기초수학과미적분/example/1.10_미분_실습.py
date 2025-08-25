from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')

f = 2*x**3 + 3*y**3

dx_f = diff(f, x)
dy_f = diff(f, y)

print(dx_f) # 6*x**2
print(dy_f) # 9*y**2

# 함수 그래프 그리기
plot3d(f, (x, -10, 10), (y, -10, 10))