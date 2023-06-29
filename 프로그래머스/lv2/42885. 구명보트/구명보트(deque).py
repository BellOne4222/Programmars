from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    answer = 0

    while people:
        maximum = people.pop()
        left = limit - maximum
        if people and (left >= people[0]):
            people.popleft()
        
        answer = answer + 1
        
    return answer

print(solution([70, 50, 80, 50], 100))