def solution(phone_book):
    phone_book.sort() # 전화번호를 사전식으로 정렬하여 접두사인 번호가 함께 위치하도록 합니다.

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            # 만약 현재 번호와 다음 번호의 접두사가 같다면, 접두사가 더 긴 번호가 있다는 의미이므로 False를 반환합니다.
            return False

    # 모든 번호들의 접두사를 비교한 후 중복된 접두사가 없으면 True를 반환합니다.
    return True