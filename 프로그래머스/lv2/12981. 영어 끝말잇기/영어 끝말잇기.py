def solution(n, words):
    answer = [0, 0]
    word = [words[0]]
    
    for i in range(1, len(words)):
        if words[i] not in word:
            if words[i][0] == word[-1][-1]:
                word.append(words[i])
            else:
                answer =  [i%n + 1, i//n+1]
                break
        else:
            answer = [i%n + 1, i//n+1]
            break

    return answer