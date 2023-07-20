compare = 10 ** 6


def dfs(picks, minerals, fatigability):
    global compare

    if sum(picks) == 0 or not minerals:
        compare = min(fatigability, compare)
        return

    for i in range(len(picks)):
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
            dfs(picks, minerals[5:], fatigability + tiredCount)
            picks[i] += 1


def solution(picks, minerals):
    global compare
    dfs(picks,minerals,0)
    return compare