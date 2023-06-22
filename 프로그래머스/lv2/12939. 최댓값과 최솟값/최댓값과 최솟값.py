def solution(s):
    lst = list(map(int, s.split()))
    lst.sort()
    
    result = "{} {}".format(min(lst), max(lst))
    return result
        
        
                   
        