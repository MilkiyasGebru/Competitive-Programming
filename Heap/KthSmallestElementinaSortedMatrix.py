import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        visited = set()
        
        heapq.heappush(heap,(matrix[0][0],(0,0)))
        direction = [(1,0),(0,1)]
        
        def isVaild(row,col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix) and not (row,col) in visited
        
        def adder(row,col):
            
            visited.add((row,col))
            
            for j in direction:
                
                nr = row + j[0]
                nc = col + j[1]
                
                if isVaild(nr,nc):
                    heapq.heappush(heap,(matrix[nr][nc],(nr,nc)))
                    visited.add((nr,nc))
        
        while(k > 0): 
            
            k -=1
            ans, coordinate = heapq.heappop(heap)
            adder(coordinate[0],coordinate[1])
            
        return ans            
                    
                    
