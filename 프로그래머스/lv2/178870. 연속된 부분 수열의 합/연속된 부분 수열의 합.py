def solution(sequence, k):
    s_idx, e_idx = -1, -1
    if k not in sequence:
        n = len(sequence)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + sequence[i - 1]

        i, j = 0, 1
        while j <= n:
            current_sum = prefix_sum[j] - prefix_sum[i]
            if current_sum == k:
                if s_idx == -1 or e_idx - s_idx > j - i - 1:
                    s_idx, e_idx = i, j - 1
                i += 1
            elif current_sum < k:
                j += 1
            else:
                i += 1

    else:
        idx = sequence.index(k)
        s_idx, e_idx = idx, idx

    return [s_idx, e_idx]
    