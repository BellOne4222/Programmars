def solution(k, tangerine):
    arr = list(set(tangerine))
    tan_dict = {i:0 for i in arr}
    for j in arr:
        tan_dict[j] = tangerine.count(j)
    
    tanger_dict = dict(sorted(tan_dict.items(), key=lambda x: x[1], reverse = True))
    
    tangerines = 0
    result = 0
    while True:
        for l in tanger_dict:
            tangerines += tanger_dict[l]
            result += 1
        if tangerines >= k:
            break
    return result

from collections import Counter

def solution(k, tangerine):
    tan_counter = Counter(tangerine)
    tanger_dict = dict(sorted(tan_counter.items(), key=lambda x: x[1], reverse=True))
    
    tangerines = 0
    result = 0
    for tangerine, count in tanger_dict.items():
        if tangerines >= k:
            break
        tangerines += count
        result += 1
    
    return result
print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))