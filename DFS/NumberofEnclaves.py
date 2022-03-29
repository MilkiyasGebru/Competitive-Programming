class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def isValid(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])  and grid[row][col]==1
        
        def dfs(row,col):
            
            grid[row][col] = 0
            
            for direction in directions:
                
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if isValid(new_row,new_col):
                    
                    dfs(new_row,new_col)
                    
        for i in range(0,len(grid),max(1,len(grid)-1)):
            
            for j in range(0,len(grid[0])):
                
                if grid[i][j]==1:
                    
                    dfs(i,j)
                    
        for j in range(0,len(grid[0]),max(1,len(grid[0])-1)):
            
            for i in range(0,len(grid)):
                
                if grid[i][j]==1:
                    
                    dfs(i,j)
        moves = 0            
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j]==1:
                    moves +=1
             
        return moves
