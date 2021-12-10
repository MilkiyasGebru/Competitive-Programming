class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        i=0
        j=1
        while i<len(nums):
            while i<j and j<len(nums):
                if nums[i]==nums[j]:
                    x=x+1
                j=j+1
            i = i+1   
            j = i+1
            if i+1 == len(nums) :
                return x
            if i == len(nums) :
                return x
        
