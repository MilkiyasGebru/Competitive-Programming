class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        Visited =set()
        oldColor = image[sr][sc]
        def changeColor(sr,sc):
            Visited.add((sr,sc))
            image[sr][sc]=newColor
            if sr-1 >= 0 and not (sr-1,sc) in Visited and  image[sr-1][sc]==oldColor :
                changeColor(sr-1,sc)
            if sr +1 <=len(image)-1 and not (sr+1,sc) in Visited and image[sr+1][sc]==oldColor:
                changeColor(sr+1,sc)
            if sc-1 >=0 and not (sr,sc-1) in Visited and image[sr][sc-1]==oldColor:
                changeColor(sr,sc-1)
            if sc+1 <=len(image[0])-1 and not (sr,sc+1) in Visited  and image[sr][sc+1]==oldColor:
                changeColor(sr,sc+1)
        changeColor(sr,sc)
        return image
        

            
