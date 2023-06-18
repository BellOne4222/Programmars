def solution(dartResult):
    num = ''
    answers = []
    for i in dartResult:
        if i.isnumeric():
            num += i
        elif i == "S":
            score = pow(int(num), 1)
            answers.append(score)
            num = ''
        elif i == "D":
            score = pow(int(num), 2)
            answers.append(score)
            num = ''
        elif i == "T":
            score = pow(int(num), 3)
            answers.append(score)
            num = ''
        elif i == "*":
            if len(answers) >= 2:
                answers[-2] *= 2
                answers[-1] *= 2
            else:
                answers[-1] *= 2
        elif i == "#":
                answers[-1] *= -1
        
    answer = sum(answers)
    return answer

            
            
        
            
    
    
        
                
                    
                
                
            