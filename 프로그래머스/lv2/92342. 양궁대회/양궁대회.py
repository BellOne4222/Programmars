maxScore = 0       # 가장 큰 점수 차이
maxList = []       # 가장 큰 점수 차이를 낸 배열 

# ryanScore(index, score, n, apeach): 이 함수는 DFS(Depth-First Search) 방식을 사용하여 가능한 모든 경우의 수를 탐색합니다. index는 현재까지 확인한 점수의 인덱스, score는 라이언의 점수를 나타내는 배열, n은 남은 공격 횟수, apeach는 어피치의 각 점수에 해당하는 배열입니다. 이 함수는 횟수가 0일 때 calScore() 함수를 호출하고 반환합니다.

def ryanScore(index, score, n, apeach) :    # dfs 함수
    if n == 0 :               # 횟수가 0 이면 calScore() 호출
        calScore(score, apeach)
        return
    
    if index == 11: return    # 0~10까지의 점수만 존재
    
    sc = apeach[index]         # 어피치가 (index)점을 맞힌 횟수
    for i in range(sc+2):    # 0부터 (index)+1까지 맞히는 경우만 고려
        if n >= i:           # n보다 크면 안되니까 고려
            score[index] = i
            ryanScore(index+1, score, n-i, apeach)
            score[index] = 0    
    
# calScore(ryan, apeach): 이 함수는 라이언과 어피치의 점수를 계산하여 최대 점수 차이를 구하고, 그에 해당하는 점수 배열을 maxList에 저장합니다. ryan과 apeach는 각각 라이언과 어피치의 점수 배열을 나타냅니다. 이 함수에서는 라이언과 어피치가 0점이 아닌 점수를 맞혔을 때에만 점수를 계산합니다. 라이언의 점수가 어피치보다 높을 경우 라이언은 해당 점수에 대해 (10 - i)만큼의 점수를 획득하고, 어피치는 점수를 획득하지 못합니다. 이후 최대 점수 차이를 계산하여 maxScore와 maxList를 갱신합니다.
def calScore(ryan, apeach):    # 점수 계산 함수
    global maxScore, maxList
    rScore = 0    # 라이언 점수
    aScore = 0    # 어피치 점수
    
    for i in range(11):
        if ryan[i] == 0 and apeach[i] == 0: continue    # 둘다 0이면 패스
        
        if ryan[i] > apeach[i] : rScore += (10-i)    # 라이언이 더 많이 맞췄으면 점수획득
        else : aScore += (10-i)               # 아니면 어피치 점수획득
        
    if rScore > aScore :    # 라이언 점수가 더 높을 때만 고려
        diff = rScore - aScore
        if diff > maxScore:    # 최대값 갱신
            maxScore = diff
            maxList = list(ryan)
            
        elif diff == maxScore:            # 최대값이 같을 경우
            for i in range(11):    
                if ryan[-i] > maxList[-i]:    # 낮은 점수를 많이 맞은 경우가 선택
                    maxList = list(ryan)
                    break
                elif ryan[-i] < maxList[-i]:
                    break
                    
# solution(n, info): 이 함수는 주어진 입력에 대해 문제를 해결합니다. n은 남은 공격 횟수를 나타내고, info는 어피치가 각 점수에 대해 맞힌 횟수를 나타내는 배열입니다. 이 함수에서는 임시로 0으로 초기화된 배열 temp을 생성한 후, ryanScore() 함수를 호출하여 가능한 모든 경우의 수를 탐색합니다. 마지막으로 maxList의 길이가 0인 경우 -1을 반환하고, 그렇지 않은 경우 maxList를 반환합니다.
def solution(n, info):
    temp = [0 for i in range(11)]
    ryanScore(0, temp, n, info)    # dfs
    
    if len(maxList)==0 : return [-1]
    else: return maxList







