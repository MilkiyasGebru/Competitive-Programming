class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        old_color = grid[row][col]
        visited = set()
        marked = set()
        
        def isValid(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and  grid[row][col] == old_color
        
        def dfs(row,col):
            
            visited.add((row,col))
            b= True
            for direction in directions:
                
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                valid = isValid(new_row,new_col)
                b = b and valid
                
                if valid and (new_row,new_col) not in visited:
                    dfs(new_row,new_col)
            if not b:
                marked.add((row,col))
                
        dfs(row,col)
        
        for i in marked:
            grid[i[0]][i[1]]=color
        return grid  
