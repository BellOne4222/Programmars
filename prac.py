def solution(topping):
    
    # 자르는 경우의 수
    case = 0
    
    num = 0
    # 1. 토핑 길이가 짝수일 때, 홀수일 때 경우 나눠서 반씩 나누기
    
    # 철수
    elder = []
    # 동생
    younger = []
    
    new_elder = []
    new_younger = []
    
    
    # 짝수일 때
    if len(topping) % 2 == 0:
        num = int(len(topping) / 2)
        elder = topping[0:num]
        younger = topping[num:len(topping)]
        print(num, elder, younger)
        
    # 2. 반으로 나눈 집합 2개 중복 제거
        new_elder = list(set(elder))
        new_younger = list(set(younger))
        
        if len(new_elder) == len(new_younger):
            case += 1
        elif len(new_elder) > len(new_younger):
            pass
        else:
            pass
        
        
        
    
    # 홀수일 때
    else:
        num = int(len(topping) / 2)
        elder = topping[0:num]
        younger = topping[num:len(topping)]
        print(num, elder, younger)
        
    # 2. 반으로 나눈 집합 2개 중복 제거
        new_elder = list(set(elder))
        new_younger = list(set(younger))
        
        if len(new_elder) == len(new_younger):
            case += 1
        elif len(new_elder) > len(new_younger):
            pass
        else:
            pass
        
    
    # 3. 중복 제거한 두 집합 각각의 원소 개수 비교해서 같아 질때까지 반복
    
    # 4. 중복 제거한 topping 길이가 홀수이면, break하고 0반환
    
    
    