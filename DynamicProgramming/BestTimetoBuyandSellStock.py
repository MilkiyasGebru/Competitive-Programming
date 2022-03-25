class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = [[prices[0],0]]
        last = []
        i=1
        while(i < len(prices)):
            if  len(first) > len(last) and  first[-1][0] > prices[i] :
                
                first.pop()
                first.append([prices[i],i])
                
            elif len(first)==len(last) and first[-1][0] > prices[i]:
                first.append([prices[i],i])
                
            elif len(first) == len(last) and  last[-1][0] < prices[i]:
                last.pop()
                last.append([prices[i],i])
            elif len(first) > len(last) :
                last.append([prices[i],i])
            i=i+1   
        answer=0        
        if len(last)==0:
            return 0
        else:
            for i in range(len(last)):
                answer = max(last[i][0]-first[i][0],answer)
            return answer 
