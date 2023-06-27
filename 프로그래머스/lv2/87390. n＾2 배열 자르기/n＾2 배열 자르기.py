def solution(n, left, right):
    result = []
    
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        
        max_val = max(row, col)
        value = max_val + 1
        
        result.append(value)
    
    return result