# 1차 failed

def solution(scoville, K):
    # 안 매운 순으로 정렬
    scoville.sort()
    
    mixing = 0
    
    while True:
        a = 0
        b = 0
        if all(i >= 7 for i in scoville):
            return mixing
            break
        elif len(scoville) == 0:
            mixing = -1
            break
        
        a = scoville.pop(0)
        b = scoville.pop(0)
        
        new = a + (b*2)
        
        scoville.insert(0,new)
        mixing += 1
    
    return mixing