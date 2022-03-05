# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
 
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while(queue):
            header1 = queue.pop()
            header2 = queue.pop()
            if header1 and header2 and header1.val == header2.val:
                queue.append(header1.left)
                queue.append(header2.right)
                queue.append(header1.right)
                queue.append(header2.left)
            elif header1==None and header2==None:
                continue
            else:
                return False
        return True   
            
                
