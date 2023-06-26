def solution(n):
    tentotwo = str(bin(n))[2:]
    cnt_one = tentotwo.count("1")
    next_n = n+1
    result = 0

    while True:
    
        next_tentotwo = str(bin(next_n))[2:]
        next_cnt_one = next_tentotwo.count("1")
        
        if next_cnt_one == cnt_one:
            result = next_n
            break
        else:
            next_n += 1
    
    
    return result
        
        
        