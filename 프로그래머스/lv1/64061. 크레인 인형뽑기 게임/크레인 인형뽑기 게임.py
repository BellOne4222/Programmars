def solution(board, moves):
    doll_board = [[] for _ in range(len(board[0]))]
    for j in range(len(board)):
        for i in range(len(board[0])):
            if board[i][j] == 0:
                pass
            else:
                doll_board[j].append(board[i][j])
    count = 0
    basket = []
    for i in range(len(moves)):
        if len(doll_board[moves[i]-1]) == 0:
            continue
        else:
            basket.append(doll_board[moves[i]-1][0])
            del doll_board[moves[i]-1][0]
            
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            for i in range(2):
                basket.pop()
            count += 1
    result = count * 2
    
    return result
        
        
        
        
        
            
    
    
            
    
        
            
    
        
            
            