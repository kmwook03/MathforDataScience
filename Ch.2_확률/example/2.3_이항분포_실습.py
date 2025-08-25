"""
밑바닥부터 이항 분포 구현
"""

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

def binomial_coefficient(n: int, k: int) -> float:
    '''
    이항 계수 계산 함수
    
    Args:
        n (int): 시행 횟수
        k (int): 성공 횟수
    Returns:
        float: C(n,k) 계산 결과
    '''
    return factorial(n) / (factorial(k) * factorial(n - k))

def binomial_distribution(n: int, k: int, p: float) -> float:
    '''
    이항 분포 확률 계산 함수

    Args:
        n (int): 시행 횟수
        k (int): 성공 횟수
        p (float): 성공 확률
    Returns:
        float: 이항 분포 확률 계산 결과
    '''
    return binomial_coefficient(n, k) * (p ** k) * ((1.0 - p) ** (n - k))

n = 10
p = 0.9

for k in range(n + 1):
    probability = binomial_distribution(n, k, p)
    print("{0} - {1}".format(k, probability))