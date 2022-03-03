class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        province=0
        n = len(isConnected)
        
        def dfs(row,col,n):
            isConnected[row][col]=0
            
            for x in range(n):
                if isValid(col,x,n):
                    dfs(col,x,n)
                    
        def isValid(row,col,n):
            return 0 <= row < n and 0 <= col < n and isConnected[row][col]==1  
        
        for i in range(n):
            
            for j in range(n):
                
                if  isConnected[i][j]==1:

                    province +=1
                    dfs(i,j,n)
                    
        return province            
