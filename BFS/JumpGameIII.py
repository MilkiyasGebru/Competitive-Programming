class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        value = set()
        
        direction = [-1,1]
        
        queue = deque()
        queue.append(start)
        visited.add(start)
        
        
        def isValid(i):
            
            return 0 <= i < len(arr) and not i in visited
        
        def bfs(i):
            
            for j in direction:
              
                inew = i + j*arr[i]
                
                if isValid(inew):
                    
                    visited.add(inew)
                    queue.append(inew)
            
        
        while(queue):
            
            valid = len(queue)
            
            while(valid > 0):
                
                valid -= 1
                header = queue.popleft()
            
                if arr[header]==0:
                    return True
                bfs(header)
                
                
        return False        
                
        
        
        
        
        
