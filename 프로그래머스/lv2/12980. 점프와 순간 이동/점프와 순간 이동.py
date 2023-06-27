def solution(n):
    battery = 0
    distance = 0
    
    while True:
        if n == 0:
            break
        if n % 2 == 0: 
            n /= 2
        else:
            n -= 1
            battery += 1
    
    return battery
            
    
    
    
    