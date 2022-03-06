from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        direction =[(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        time = 0
        def checker():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        return True
            return False        
        def changer(row,col,queue):
            visited.add((row,col))
            for j in direction:
                nr = row + j[0]
                nc = col + j[1]
                if isValid(nr,nc):
                    grid[nr][nc] = 2
                    queue.append([nr,nc])

        def isValid(row,col):
            return 0 <= row < len(grid) and 0<= col < len(grid[0]) and grid[row][col] == 1 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j]==0:
                    visited.add((i,j))
  
        while(queue and checker()):
            
            valid = len(queue)

            while(valid > 0):
                valid -=1
                header = queue.popleft()
                changer(header[0],header[1],queue)
   
            time +=1

        if checker() :
            return -1
        else:
            return time
                
    
            
