def solution(s):
    stack = []
    for i in s:
        
        if len(stack) == 0:
            stack.append(i)
            
        elif stack[-1] == i:
            stack.pop()
            
            
        else:
            stack.append(i)
    
    
    
    if len(stack) == 0:
        result = 1
    elif len(stack) > 0:
        result = 0
    
    return result