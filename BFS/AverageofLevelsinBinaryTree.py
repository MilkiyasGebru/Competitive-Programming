# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        average=[]
        queue.append(root)
        
        while(queue):
            
            valid = len(queue)
            avg=0.0
            count=0
            while(valid >0):
                valid -=1
                header = queue.popleft()
                
                if header:
                    count +=1 
                    avg += header.val;
                    queue.append(header.left)
                    queue.append(header.right)
                    
            if count !=0:
                
                average.append(avg/count)   
        return average       
                
            
        
        
