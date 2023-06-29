def solution(people, limit):
    boat = 0
    people = sorted(people)
    
    LW_idx = 0 # 가장 무게가 가벼운 사람의 인덱스
    HW_idx = len(people) - 1 # 가장 무게가 무거운 사람의 인덱스
    
    while LW_idx < HW_idx:
        if people[LW_idx] + people[HW_idx] <= limit:
            LW_idx += 1
            HW_idx -= 1
        else:
            HW_idx -= 1
            
        boat += 1
        
    if LW_idx == HW_idx:
        boat += 1
    
    return boat
            
            
                
                
        
        
            
        
    

        
        