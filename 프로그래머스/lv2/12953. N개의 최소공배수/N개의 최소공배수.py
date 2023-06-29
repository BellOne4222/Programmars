def solution(arr):
    LCM = max(arr)
    
    while True:
        cnt = 0
        for i in arr:
            if LCM % i == 0:
                cnt += 1
            else:
                break
        if cnt == len(arr):
            break
        LCM += 1
        
    return LCM
    
        
        
        
    
    
    


    
    
    
            
        
        
        
        
        
            
                