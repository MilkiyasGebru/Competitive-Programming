class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left =  0
        right = len(nums)-1
        unord = 0
        Max = nums[0]
        while(left <= right):
            mid =(left + right)//2
            if nums[mid] < Max :
                unord = mid
                right = mid -1 
            else:
                Max = nums[mid]
                left = mid +1 
         
        def search(left,right):
            
            while(left<=right):
                
                mid = (left + right)//2
                
                if nums[mid]>target:
                    right = mid - 1
                elif nums[mid]<target:
                    left = mid + 1
                else:
                    return mid
                
            return -1
        if unord == 0:
            return search(0,len(nums)-1)
        else:
            return max(search(0,unord-1),search(unord,len(nums)-1))
