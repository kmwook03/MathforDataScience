# --- 문제 ---
# 동전을 19번 던졌는데 앞면이 15번, 뒷면이 4번 나왔다.
# 이 동전이 공정할 확률은? 그 이유는?

# --- 풀이 ---
# 기본 확률 = 0.50
# alpha = 15
# beta = 4
# 베타분포에서 50%보다 클 확률이 0.996이므로 공정하지 않을 가능성이 매우 높음

def factorial(n: int) -> int:
    '''
    팩토리얼 계산 함수

    Args:
        n (int): 팩토리얼 계산에 사용되는 정수(여기서는 시행 횟수)
    Returns:
        int: n! 계산 결과
    '''
    f = 1
    for i in range(n):
        f *= (i + 1) # 1부터 n까지 곱셈
    
    return f


def approximate_integral(a: float, b: float, n: int, f: callable) -> float:
    '''
    주어진 함수 f에 대해 [a, b] 구간 수치 적분

    Args:
        a (float): 구간 최소값
        b (float): 구간 최대값
        n (int): 나눠질 직사각형 개수
        f (callable): 적분할 함수
    Returns:
        float: 함수 f 적분 결과
    '''
    delta_x = (b - a) / n # 구간 너비 / 개수
    total_sum = 0

    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1)) # 중간점
        total_sum += f(midpoint) # 함수 f의 중간점 높이 합
    
    return total_sum * delta_x

def beta_distribution(x: float, alpha: float, beta: float) -> float:
    '''
    베타 분포의 확률 밀도 함수 계산

    Args:
        x (float): 기본 확률
        alpha (float): 성공 횟수
        beta (float): 실패 횟수
    Returns:
        float: 확률 밀도
    '''
    if x < 0.0 or x > 1.0:
        raise ValueError("x는 0.0과 1.0 사이여야 함.")

    numerator = (x ** (alpha - 1.0)) * ((1.0 - x) ** (beta - 1.0))
    denominator = (1.0 * factorial(alpha - 1) * factorial(beta - 1)) / \
                (1.0 * factorial(alpha + beta - 1))

    return numerator / denominator

greater_than_50 = approximate_integral(a=0.50, b=1.0, n=19,
                                       f=lambda x: beta_distribution(x, 15, 4)) # 기본 확률이 50% 이상일 확률
less_than_50 = 1.0 - greater_than_50 # 기본 확률이 50% 이하일 확률

print("50%보다 클 확률: {0}, 50%보다 작을 확률: {1}".format(greater_than_50, less_than_50))