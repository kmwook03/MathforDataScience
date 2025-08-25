from sympy import *

x, i, n = symbols('x i n')

# 함수 정의 및 구간 설정
f = x**2 + 1
lower, upper = 0, 1

# 직사각형 너비와 높이 계산
delta_x = (upper - lower) / n # 직사각형 너비
x_i = (lower + delta_x * i) # 직사각형의 x 좌표
fx_i = f.subs(x, x_i) # 직사각형의 높이

n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit() # 직사각형 넓이의 합

area = limit(n_rectangles, n, oo) # 직사각형 개수 n을 무한대로
print(area) # 4/3