def solution(phone_book):
    phone_book.sort() # 전화번호 책 정렬

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            # 전화번호를 두개씩 비교하여 지금 전화번호와 다음 전화번호의 접두사가 같으면 false 반환
            return False

    # 모든 번호들의 접두사를 비교한 후 중복된 접두사가 없으면 True를 반환
    return True