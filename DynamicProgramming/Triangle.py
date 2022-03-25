class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        def recursive(row,col):
            
            if row >=len(triangle):
                return 0
            
            if (row+1,col) not in f:
                f[(row+1,col)]=recursive(row+1,col)
                
            if (row+1,col+1) not in f:
                f[(row+1,col+1)]= recursive(row+1,col+1)
            
            return min(triangle[row][col]+f[(row+1,col)],triangle[row][col]+f[(row+1,col+1)])
          
        f={}
        
        return recursive(0,0)
