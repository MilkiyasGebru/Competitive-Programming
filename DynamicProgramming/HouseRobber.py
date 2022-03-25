class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def recursive(index):
            if index >= len(nums):
                return 0
            if index + 1 not in f:
                f[index+1] = recursive(index + 1)
            if index + 2 not in f:
                f[index+2] = recursive(index + 2)
            
            return max(nums[index]+f[index+2],f[index+1])
        f={}
        return recursive(0)
