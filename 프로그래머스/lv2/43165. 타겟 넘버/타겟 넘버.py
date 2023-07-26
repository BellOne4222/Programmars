result = 0

def dfs(numbers, target, case_cnt, num):
    global result
    if case_cnt == len(numbers):
        if num == target:
            result += 1
        return 
    
    dfs(numbers, target, case_cnt+1, num + numbers[case_cnt])
    dfs(numbers, target, case_cnt+1, num - numbers[case_cnt])
    
        
        

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return result
