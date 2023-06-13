def solution(ingredient):
    hamburger = [1, 2, 3, 1]
    kitchen = []
    count = 0
    for i in ingredient:
        kitchen.append(i)
        if kitchen[-4:] == hamburger:
            count += 1
            for j in range(4):
                kitchen.pop()
    return count
        
        
        
    
    