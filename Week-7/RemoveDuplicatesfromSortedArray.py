class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=0
        index=0
        end=len(nums)-1
        k=1
        while(not start==len(nums)-1):
            if(nums[start]==nums[start+1]):
                start +=1
            else:
                k +=1
                nums[index],nums[start]=nums[start],nums[index]
                index +=1
                start +=1
        nums[k-1],nums[end]=nums[end],nums[k-1]        
        return k        
