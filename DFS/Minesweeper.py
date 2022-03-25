class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        visited = set()
        direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        def isValid(row,col):
                
            return 0 <= row < len(board) and 0 <= col < len(board[0]) and (row,col) not in visited 
        
        def dfs(row,col):
            
            visited.add((row,col))
            counter = 0
            
            
            for j in direction:
                
                new_row = row + j[0]
                new_col = col + j[1] 
                
                if isValid(new_row,new_col):
                    
                    if board[new_row][new_col]=="M":
                        counter += 1

            if counter != 0 :
                board[row][col] = str(counter)
                
            else:
                
                board[row][col] = 'B'
                
                for j in direction:
                    
                    new_row = row + j[0]
                    new_col = col + j[1] 
                    
                    if isValid(new_row,new_col):
                        
                        dfs(new_row,new_col)

                
        if board[click[0]][click[1]]=="M":
            
            board[click[0]][click[1]]="X"
            return board
        
        else:
            
            dfs(click[0],click[1])
            return board
                
            
            
            
