from collections import deque

def solution(maps):
    # 이동 방향에 따른 x,y 정의
    dx = [1,-1,0,0] # 동서남북
    dy = [0,0,1,-1]
    
    n = len(maps[0])
    m = len(maps)
    # 가장 가까운 칸부터 가므로 bfs 사용
    def bfs(x,y):
        n = len(maps[0])
        m = len(maps)
        
        adventure = deque()
        adventure.append((x,y))

        while adventure:
            x, y = adventure.popleft()
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]

                if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                    continue
                if maps[next_x][next_y] == 0:
                    continue
                if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] = maps[x][y] + 1
                    adventure.append((next_x,next_y))

        return maps[n-1][m-1]
    
    
    answer = bfs(0,0)
    
    if answer == 1:
        answer = -1
    else:
        return answer
    
    