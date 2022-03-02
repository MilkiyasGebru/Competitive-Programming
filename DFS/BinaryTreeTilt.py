class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def summer(root):
            if root==None:
                return 0
            else:
                return root.val + summer(root.left) + summer(root.right)
        def finder(root):
            if root==None:
                return 0
            else:
                return  abs(summer(root.left)-summer(root.right))+finder(root.left)+finder(root.right)
            
        return finder(root)
