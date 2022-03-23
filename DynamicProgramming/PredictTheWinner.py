class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        f={}
        def recursive(x,y):
            
            if x > y:
                
                return 0
            if (x+1,y) not in f:
                f[(x+1,y)]=recursive(x+1,y)
            if (x,y-1) not in f:
                f[(x,y-1)]=recursive(x,y-1)
            return max(nums[x]-f[(x+1,y)],nums[y]-f[(x,y-1)])
        
        
        if recursive(0,len(nums)-1)>= 0:
            return True
        else:
            return False
        
