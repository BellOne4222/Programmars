def solution(targets):
    targets = sorted(targets)
    misail = 1
    current = targets[0]
    start, end = current[0], current[1]
    for i in range(1, len(targets)):
        if targets[i][0] > end:
            misail += 1
            current = targets[i]
            start, end = current[0], current[1]
        else:
            if targets[i][1] < end:
                end = targets[i][1]
    
    return misail

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))