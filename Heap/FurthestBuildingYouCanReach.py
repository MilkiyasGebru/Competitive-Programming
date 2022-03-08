class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap =[]
        current =0
        
        while(current + 1 < len(heights)):
            
            distance = heights[current + 1] - heights[ current ]
            
            if distance <=0 :
                
                current += 1
                
            else:
                
                if (ladders > 0):
                    
                    heapq.heappush(heap,distance)
                    ladders -=1
                    current +=1
                    
                else:
                    
                    dis = heapq.heappushpop(heap,distance)
                    
                    if bricks >= dis:
                        
                        bricks -= dis
                        current += 1
                        
                    else:
                        break
                        
        return current             
    
