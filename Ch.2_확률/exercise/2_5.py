# --- 문제 ---
# 라스베이거스 댈러스행 항공편에 137명의 승객이 예약되어 있다.
# 하지만 일요일 아침 라스베이거스에 각 승객이 나타나지 않을 확률은 40%다.
# 비행기가 빈 채로 비행하지 않도록 초과 예약할 좌석 수를 파악하려고 한다.
# 적어도 50명의 승객이 나타나지 않을 가능성은 얼마인가?

# --- 풀이 ---
# n = 137
# p = 0.40
# k = 50 ~ 137
# 이항 분포의 50 이상 확률의 누적합을 구하자

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

n = 137
p = 0.40
accumulate_prob = 0
for k in range(50, n + 1):
    accumulate_prob += binomial_distribution(n, k, p)

print(accumulate_prob)