def solution(citations):
    arr = sorted(citations)
    max_h = 0
    for h in range(max(citations)+1):
        cnt = 0
        for idx in range(len(arr)):
            if arr[idx] >= h:
                cnt += 1
            if cnt == h:
                max_h = cnt
    return max_h
            
            
# def solution(citations):
#     answer = 0
#     citations.sort()
#     max_check = 0
#     for h in range(max(citations)+1):
#         cnt = 0
#         for idx in range(len(citations)):
#             if h <= citations[idx]:
#                 cnt += 1
#             if cnt == h:
#                 answer = cnt
#                 max_check = max(max_check,answer)
#     # 테케 11번이 뭐지?
#     return max_check
        
        
    
    


# [ 1,3,9,7,2,8,5,6,4,0 ]

# 위와 같은 예시가 있습니다.

 

# h번 이상 인용된 논문이 h 편 이상이다는 말은

 

# 1(h) 번 이상 인용된 논문 =   9편  >=  1(h) 편 이상

# 2(h) 번 이상 인용된 논문 =   8편  >=  2(h) 편 이상

# 3(h) 번 이상 인용된 논문 =   7편  >=  3(h) 편 이상

# 4(h) 번 이상 인용된 논문 =   6편  >=  4(h) 편 이상

# 5(h) 번 이상 인용된 논문 =   5편  >=  5(h) 편 이상

# 6(h) 번 이상 인용된 논문 =   4편  <    6(h) 편 미만 
            
            
            
        
                
        
    