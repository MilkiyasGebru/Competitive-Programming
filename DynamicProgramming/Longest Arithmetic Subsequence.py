class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        f = defaultdict(int)
        answer = 0
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(-510,501):
                f[(nums[i],j)] = max(f[(nums[i]+j,j)] + 1, f[(nums[i],j)])
                answer = max(answer,f[(nums[i],j)])
        
        return answer
