def solution(priorities, location):
    # 만약 우선순위 리스트의 길이가 1이라면, 그 문서는 1번째로 인쇄됨.
    if len(priorities) == 1:
        return 1

    length = len(priorities)  # 우선순위 리스트의 길이 저장
    cnt = 1  # 인쇄 순서 카운터 초기화 (처음에 1로 초기화하고 시작)
    candidate = priorities.pop(0)  # 우선순위 리스트의 첫 번째 문서를 후보로 지정

    while priorities:  # 아직 인쇄해야 할 문서가 남아있는 동안 반복
        if location > 0:  # 특정 문서를 찾지 못한 경우 (location이 0보다 큰 경우)
            if candidate < max(priorities):  # 후보 문서보다 더 우선순위가 높은 문서가 존재하는 경우
                priorities.append(candidate)  # 후보 문서를 맨 뒤로 이동시킴 (다시 큐의 맨 뒤로 가게 됨)
            else:  # 후보 문서가 가장 우선순위가 높은 경우
                cnt += 1  # 해당 문서를 인쇄하고 인쇄 순서 카운터를 증가시킴
            location -= 1  # 다음 문서로 이동하기 위해 위치 값을 1 감소시킴

        else:  # 특정 문서를 찾은 경우 (location이 0 이하인 경우)
            if candidate < max(priorities):  # 후보 문서보다 더 우선순위가 높은 문서가 존재하는 경우
                priorities.append(candidate)  # 후보 문서를 맨 뒤로 이동시킴 (다시 큐의 맨 뒤로 가게 됨)
                location = len(priorities) - 1  # 위치 값을 큐의 맨 뒤로 갱신 (인덱스는 0부터 시작하므로 길이 - 1)
            else:  # 후보 문서가 가장 우선순위가 높은 경우
                break  # 해당 문서를 인쇄하고 반복 종료

        candidate = priorities.pop(0)  # 다음 후보 문서를 선택하기 위해 큐에서 첫 번째 문서를 꺼냄

    # 인쇄할 숫자가 가장 마지막에 나왔을 경우 (큐에 남은 문서가 없을 경우)
    if not priorities:
        answer = length  # 전체 문서의 개수가 정답
    else:  # 아직 인쇄해야 할 문서가 남아있는 경우
        answer = cnt  # 현재까지 인쇄한 문서의 개수가 정답

    return answer  # 최종 정답 반환