from collections import deque
import itertools

import sys
sys.setrecursionlimit(1000000)

def solution(elements):
    arr = deque(elements)
    sums = []
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            sum_arr = sum(list(itertools.islice(arr,0,i)))
            sums.append(sum_arr)
            a = arr.popleft()
            arr.append(a)
    
    result = list(set(sums))
    
    return len(result)

    
        
    
    
            
        
    
        

    