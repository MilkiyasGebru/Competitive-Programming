class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = len(nums)
        a = [0]*x
        for i in range(0,x):
            for j in range(0,x):
                if i!=j and nums[i]>nums[j]:
                    a[i]=a[i]+1
        return a            
