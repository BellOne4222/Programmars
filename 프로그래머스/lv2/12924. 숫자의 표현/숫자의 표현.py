def solution(n):
    result = 0
    for i in range(1, n+1):
        sum = 0
        j = i
        while sum < n:
            sum += j
            j += 1
            if sum == n:
                result += 1
                break
    return result
                    
    
    
    