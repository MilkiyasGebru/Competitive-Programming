class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Recursive Approach"""
        f={}
        def recursive(i):
            
            if i >= len(cost):
                
                return 0
            
            else:
                
                if(i+1)>=len(cost) or (i+2)>=len(cost):return recursive(i+2)
                
                if i+2 not in f:
                    f[i+2]=recursive(i+2)
                if i+1 not in f:
                    f[i+1]=recursive(i+1)
                return min(cost[i+2]+f[i+2],cost[i+1]+f[i+1]) 
            
        return min(cost[0]+recursive(0),cost[1]+recursive(1))    

        
