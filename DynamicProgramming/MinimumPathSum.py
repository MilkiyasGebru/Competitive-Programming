class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        f={}
        def recursive(row,col):
            
            if row == len(grid)-1 and col == len(grid[0])-1:
                
                return grid[row][col]
            
            
            elif row == len(grid)-1 and col < len(grid[0])-1:
                
                if (row,col+1) not in f:
                    f[(row,col+1)] = recursive(row,col+1)
                
                return grid[row][col] + f[(row,col+1)]
            
            elif row < len(grid)-1 and col == len(grid[0])-1:
                
                if (row+1,col) not in f:
                    f[(row+1,col)] = recursive(row+1,col)

            
                return grid[row][col] + f[(row+1,col)]
            
            if (row+1,col) not in f:
                f[(row+1,col)] = recursive(row+1,col)
                
            if (row,col+1) not in f:
                f[(row,col+1)] = recursive(row,col+1)
            
            return min(grid[row][col]+f[(row+1,col)],grid[row][col]+f[(row,col+1)])
        return recursive(0,0)
        
        
