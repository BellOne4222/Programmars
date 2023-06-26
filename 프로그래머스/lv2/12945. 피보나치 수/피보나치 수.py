memo = {0:0, 1:1} # 메모리 사용

def solution(n):
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n] % 1234567
    