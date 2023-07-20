answer = 25 * 55
def solution(picks, minerals):
    global answer
    dfs(picks,minerals,0)
    return answer

def dfs(picks, minerals, tiredness):
    global answer

    if sum(picks) == 0 or not minerals:
        answer = min(tiredness, answer)
        return

    for i in range(3):
        tiredCount = 0
        if picks[i] >= 1:
            picks[i] -= 1
            mined = minerals[:5]
            if i == 0:
                tiredCount += len(mined)
            elif i == 1:
                for mineral in mined:
                    if mineral == "diamond":
                        tiredCount += 5
                    else:
                        tiredCount += 1
            elif i == 2:
                for mineral in mined:
                    if mineral == "diamond":
                        tiredCount += 25
                    elif mineral == "iron":
                        tiredCount += 5
                    else:
                        tiredCount += 1
            dfs(picks, minerals[5:], tiredness + tiredCount)
            picks[i] += 1