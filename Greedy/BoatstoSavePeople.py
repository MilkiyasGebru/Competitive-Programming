class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        people.sort()
        
        start = 0
        boat = 0
        
        end = len(people)-1
        
        while(start <= end):
            
            if people[end] + people[start] <= limit:
                
                boat +=1
                start +=1
                end -=1
                
            else :
                
                boat +=1
                end -=1
                
                
        return boat        
