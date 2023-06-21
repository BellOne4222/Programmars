def solution(n, arr1, arr2):
    lst1 = []
    for i in arr1:
        a = bin(i)
        a = a[2:]
        if len(a) < n:
            a = a.zfill(n)
            lst1.append(a)
        else:
            lst1.append(a)
    
    lst2 = []
    for j in arr2:
        b = bin(j)
        b = b[2:]
        if len(b) < n:
            b = b.zfill(n)
            lst2.append(b)
        else:
            lst2.append(b)
    answer = ['' for _ in range(n)]
    
    for k in range(n):
        for l in range(n):
            if lst1[k][l] == "1" or lst2[k][l] == "1":
                answer[k] += "#"
            else:
                answer[k] += " "
    return answer
                
                
    
            
        
            