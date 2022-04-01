class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        right = max(nums)
        left = 1
        ans =sum(nums)
        
        while(left <= right):
            mid = (left + right)//2
            Sum=0
            
            for i in range(len(nums)):
                Sum += math.ceil(nums[i]/mid)
                
            if threshold >= Sum:
                ans = min(ans,mid)
                right = mid - 1
                
            else:
                left = mid + 1 
        return ans  
