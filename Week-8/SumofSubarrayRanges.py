class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        sum =0   
        left =0
        right =0
        while(left < len(nums)):
            diff = 0
            Min = nums[left]
            Max = nums[left]
            right = left +1
            while(right < len(nums)):
                if nums[right] > Max:
                    Max = nums[right]
                elif nums[right] < Min:
                    Min = nums[right]    
                right +=1    
                diff = Max - Min   
                sum += diff
            left = left +1
        return sum
