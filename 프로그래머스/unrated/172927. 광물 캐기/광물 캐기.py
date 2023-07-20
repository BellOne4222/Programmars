def dfs(picks, minerals, fatigability):
    global result

    if sum(picks) == 0 or not minerals:
        result = min(fatigability, result)
        return

    for i in range(len(picks)):
        if picks[i] >= 1:
            picks[i] -= 1
            mined = minerals[:5]
            fatigue = 0

            if i == 0:  # 다이아몬드 곡괭이 일 때
                fatigue += len(mined)
            elif i == 1:  # 철 곡괭이 일 때
                for mineral in mined:
                    if mineral == "diamond":
                        fatigue += 5
                    else:
                        fatigue += 1
            elif i == 2:  # 돌 곡괭이 일 때
                for mineral in mined:
                    if mineral == "diamond":
                        fatigue += 25
                    elif mineral == "iron":
                        fatigue += 5
                    else:
                        fatigue += 1

            if fatigability + fatigue < result:
                dfs(picks, minerals[5:], fatigability + fatigue)

            picks[i] += 1


def solution(picks, minerals):
    global result
    result = 10 ** 6
    dfs(picks, minerals, 0)
    return result