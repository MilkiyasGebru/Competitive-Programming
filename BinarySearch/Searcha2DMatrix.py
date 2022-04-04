class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) - 1
        ans = right
        while(left <= right):
            
            mid = (left + right)//2
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                ans = mid
                left = mid +1
        left = 0
        right = len(matrix[0])-1
        
        while(left <= right):
            mid = (left + right )//2
            
            if matrix[ans][mid] > target:
                right = mid -1
            elif matrix[ans][mid]<target:
                left = mid + 1
            else:
                return True
