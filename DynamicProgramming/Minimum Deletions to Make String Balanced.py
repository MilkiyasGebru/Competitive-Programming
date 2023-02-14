class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        self.answer = inf
        total = sum(nums)
        def calc(arr):
            x = 0
            for i in arr:
                x += nums[i]
            
            self.answer = min(self.answer, abs(total - 2*x))
            
            
        def backtrack(i,arr):
            
            if len(arr) == len(nums) // 2:
                calc(arr)
                return
            if len(arr) + (len(nums) - i) < len(nums)//2:
                return
            
            backtrack(i+1,arr + [i])
            backtrack(i+1,arr)
        
        backtrack(0,[])
        return self.answer
