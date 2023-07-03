from collections import Counter

def solution(k, tangerine):
    tan_counter = Counter(tangerine)
    tanger_dict = dict(sorted(tan_counter.items(), key=lambda x: x[1], reverse=True))
    
    tangerines = 0
    result = 0
    for tangerine, count in tanger_dict.items():
        if tangerines >= k:
            break
        tangerines += count
        result += 1
    
    return result
            
            
        
        
                        
        