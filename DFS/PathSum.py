class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

 
        
        def depthFinder(root,depth):
            if root==None:
                return False
            depth += root.val
            if root.left==None and root.right==None and depth==targetSum:
                return True
            else:
                return depthFinder(root.left,depth) or depthFinder(root.right,depth)
        return depthFinder(root,0)  
