def solution(s):
    stack = []
    for i in s:
        if s[0] == ")":
            return False
        if len(stack) == 0:
            stack.append(i)
        elif i == ")":
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) > 0:
        return False
    elif len(stack) == 0:
        return True
        
    