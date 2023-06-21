
def solution(n):
    tentothree = ''
    while True:
        if n < 3:
            tentothree = '1'
            break
        a = n % 3
        tentothree += str(a)
        n //= 3
        if n // 3 < 1:
            tentothree += str(n)
            break
    notation = []
    for i in tentothree:
        notation.append(i)
    notation_idx = [j for j in range(len(notation))]
    threetoten = []
    
    
    
    for k in reversed(notation):
        threetoten.append(k)
    
    answer = []
    for l in range(len(threetoten)):
        b = int(threetoten[l]) * pow(3, l)
        answer.append(str(b))
        
    result = 0
    for num in answer:
        result += int(num)
    
    return result
        
    

        
    
        
        
        
        
        