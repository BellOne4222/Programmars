def solution(dartResult):
    answer = 0
    scores = []
    for i in dartResult:
        if i.isdigit() == True:
            score = int(i)
            if i.isdigit() == True and dartResult[dartResult.index(i)+1].isdigit() == True:
                a = (i+dartResult[dartResult.index(i)+1])
                score = int(a)
        elif i == "S":
            scores.append(pow(score, 1))
        elif i == "D":
            scores.append(pow(score, 2))
        elif i == "T":
            scores.append(pow(score, 3))
        elif i == "#":
            scores[-1] *= -1
        elif i == "*":
            if len(scores) <= 1:
                scores[-1] *= 2
            else:
                scores[-1] *= 2
                scores[-2] *= 2
                
    for k in scores:
        answer += k
    return answer
        
                
                    
                
                
            