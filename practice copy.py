def solution(sequence, k):
    s_idx, e_idx = 0, 0
    if k not in sequence:
        check = []
        n = len(sequence)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + sequence[i - 1]

        for i in range(n):
            for j in range(i + 1, n + 1):
                if prefix_sum[j] - prefix_sum[i] == k:
                    if check and len(check[0]) > j - i:
                        check.pop()
                        check.append(sequence[i:j])
                        s_idx, e_idx = i, j - 1
                    elif len(check) == 0:
                        check.append(sequence[i:j])
                        s_idx, e_idx = i, j - 1
    else:
        s_idx = sequence.index(k)
        e_idx = sequence.index(k)

    return [s_idx, e_idx]