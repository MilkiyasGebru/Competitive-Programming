class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        def areaCounter(sr,sc):
            grid[sr][sc] = 0
            count = 1
            for d in direction:
                nr = sr + d[0]
                nc = sc + d[1]
                if isValid(nr,nc):
                    count +=areaCounter(nr,nc)
            return count
            
        def isValid(row,col):
            return 0 <= row < len(grid) and 0 <= col <len(grid[0]) and grid[row][col]==1
        for sr in range(len(grid)):
            for sc in range(len(grid[0])): 
                if grid[sr][sc]==1:
                    max_area = max(max_area, areaCounter(sr,sc))
        

        return max_area
