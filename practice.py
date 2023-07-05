def solution(citations):
    arr = sorted(citations)
    citations_dict = {num:0 for num in arr}
    for h in range(max(citations)+1):
        cnt = 0
        for i in arr:
            if i >= h:
                cnt += 1
            if cnt < h:
                break

print(solution([3, 0, 6, 1, 5]))