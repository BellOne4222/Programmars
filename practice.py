def solution(sequence, k):
    s_idx, e_idx = 0, 0
    if k not in sequence:
        sums = 0
        a = 1
        check = []
        
        for i in range(len(sequence)-a):
            for j in range(a, len(sequence)):
                sums = sum(sequence[i:j+1])
                if sums == k:
                    if check and len(check[0]) > len(sequence[i:j+1]):
                        check.pop()
                        check.append(sequence[i:j+1])
                        s_idx, e_idx = i, j
                    elif len(check) == 0:
                        check.append(sequence[i:j+1])
                        s_idx, e_idx = i, j
                        
    else:
        s_idx = sequence.index(k)
        e_idx = sequence.index(k)
        
    return [s_idx, e_idx]