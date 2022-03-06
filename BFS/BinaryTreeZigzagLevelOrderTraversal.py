# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        values=[]
        count=0
        while(queue):
 
            valid = len(queue)
            lister=[]
            while(valid>0):
                header =queue.popleft()
                valid -=1
                if header:
                    lister.append(header.val)
                    if header.left : queue.append(header.left)
                    if header.right : queue.append(header.right) 
            if count %2 !=0: lister.reverse()        
            if len(lister) > 0: values.append(lister)
            count +=1
        return values      
                
