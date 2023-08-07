from collections import deque


# 가장 가까운 칸부터 가므로 bfs 사용
def bfs(x,y,maps,n,m):
    adventure = deque()
    adventure.append((x,y))
    
    while maps:
        x, y = adventure.popleft()
        for i in range(len(dx)):
            next_x = x + dx[i]
            next_y = x + dy[i]
            
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                continue
            if maps[next_x][next_y] == 0:
                continue
            if maps[next_x][next_y] == 1:
                maps[next_x][next_y] == maps[x][y] + 1
                adventure.append((next_x,next_y))
    result = maps[n-1][m-1]
    return
                
def solution(maps):
    
    n = len(maps[0])
    m = len(maps)
    bfs(0,0,maps,n,m)
    if result == 0:
        result = -1
    else:
        return result