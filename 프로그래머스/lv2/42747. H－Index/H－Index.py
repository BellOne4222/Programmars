def solution(citations):
    result = 0
    arr = sorted(citations)
    for i in range(len(arr)):
        if arr[i] >= len(arr) - i:
            result +=1

    return result
            
            
            
        
                
        
    