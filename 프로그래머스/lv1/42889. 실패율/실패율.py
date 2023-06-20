def solution(N, stages):
    users = len(stages)
    stages = sorted(stages)
    stage = {i:0 for i in range(1,N+1)}
    arr = [ar for ar in range(1,N+1)]
    
    for j in arr:
        if users == 0:
            stage[j] = 0
        else:
            fail = (stages.count(j)) / users
            stage[j] = fail
            users -= stages.count(j)
    
    result_dict = sorted(stage.items(), key = lambda item: item[1], reverse = True)
    result = []
    for k in range(len(result_dict)):
        result.append(result_dict[k][0])
    
    return result

    
    
        
    
    
    
    

    
    
    