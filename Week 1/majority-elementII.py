class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
    
        x = len(nums)
        nums.sort()
        y=set([])
        k=1
        for i in range(0,x):
            if i<x-1 and nums[i]==nums[i+1]:
                k=k+1
                if k>x/3 :
                    y.add(nums[i])
            elif i<x-1 and not nums[i]==nums[i+1]:
                k=1
                if k>x/3:
                    y.add(nums[i])
            if i==x-1 :
                k=1
                if k>x/3:
                    y.add(nums[i])
        return list(y)
                    
                
                
                
