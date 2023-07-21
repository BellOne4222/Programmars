from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    compare = deque([i for i in range(len(priorities))])
    
    for i in range(len(priorities)):
        c = priorities.popleft()
        c_2 = compare.popleft()
        if c < max(priorities):
            priorities.append(c)
            compare.append(c_2)
        elif c > max(priorities):
            result = compare.index(location)
            break
    
    return result + 1

print(solution([2, 1, 3, 2]	, 2))