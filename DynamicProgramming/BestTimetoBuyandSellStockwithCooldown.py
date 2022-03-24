class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f={}
        
        def calculator(n,status):
            if n >= len(prices):
                return 0
            
            if (n+1,0) not in f:
                f[(n+1,0)]=calculator(n+1,0)
             
            if (n+1,1) not in f:
                f[(n+1,1)]=calculator(n+1,1)
                
            if (n+1,2) not in f:
                f[(n+1,2)]=calculator(n+1,2)
                
            if status == 1:
                return max(prices[n]+f[(n+1,0)],f[(n+1,1)])
            
            elif status == 0:
                return f[(n+1,2)]
            
            elif status == 2:
                return max(f[(n+1,2)],f[n+1,1]-prices[n])
                
        return max(calculator(1,1)-prices[0],calculator(1,2))
