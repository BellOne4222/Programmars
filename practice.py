def solution(n):
    nums = [num for num in range(1, n+1)]
    result = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            sum = 0
            while True:
                sum += nums[j]
                if sum == n:
                    result += 1
                    break
    
    return result