class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap =[]
        n=len(grid)
        
        visited = set()

        maxSeen ={}
        
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        heapq.heappush(heap,(grid[0][0],(0,0)))
        
        def isValid(row,col):
            return 0 <= row < n and 0 <= col < n and (row,col) not in visited
        
        def changer(row,col):
            
            for j in direction:
                nr = row + j[0]
                nc = col + j[1]
                
                if isValid(nr,nc):
                    maxx = max(time,grid[nr][nc])
                    if (nr,nc) in maxSeen and maxx >= maxSeen[(nr,nc)]:
                        continue
                    heapq.heappush(heap,(maxx,(nr,nc)))
                    maxSeen[(nr,nc)] = maxx
        

        while(heap):

            time, coordinate = heapq.heappop(heap)
            x,y =coordinate

            visited.add(coordinate)
            
            if (n-1,n-1) in visited:
                return time
            changer(x,y)
            
