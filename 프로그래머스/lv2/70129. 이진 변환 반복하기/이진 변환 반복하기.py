def solution(s):
    zero_count = 0
    change_count = 0
    while True:
        zero_count += s.count("0")
        s = s.replace("0",'')
        ten_to_two = len(s)
        change_count += 1
        s = bin(ten_to_two)[2:]
        if s == "1":
            break
        
        
    return [change_count, zero_count]    
    
            
            
    