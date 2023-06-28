def right_pls(s):
    stack = []
    
    # 나중에 들어온 괄호 쌍을 먼저 처리를 해줘야 하기 때문에 LIFO 성질을 이용하기 위해서 stack 사용
    for i in s:
        if stack and stack[-1] == "(" and i == ")":
            stack.pop()
        elif stack and stack[-1] == "{" and i == "}":
            stack.pop()
        elif stack and stack[-1] == "[" and i == "]":
            stack.pop()
        else:
            stack.append(i)
    
    return len(stack) == 0 # 스택이 비어있으면 올바른 괄호 문자열이므로

def solution(s):
    x_cnt = 0
    
    for j in range(len(s)):
        if right_pls(s[j:]+s[:j]):
            x_cnt += 1
    
    return x_cnt
   