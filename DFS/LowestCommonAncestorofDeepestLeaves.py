class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def cal(root):
            
            if root == None:
                return 0
            
            else:
                if root.left not in f:
                    
                    f[root.left]=cal(root.left)
                    
                if root.right not in f:
                    
                    f[root.right]=cal(root.right)
                    
                return max(1+f[root.left],1+f[root.right] )
        
        def dfs(root):
            
            left = cal(root.left)
            right = cal(root.right)
            
            if left > right   :
                return dfs(root.left)
            
            elif right > left :
                return dfs(root.right)
            
            else:
                return root
            
        f ={}
        return dfs(root)    
