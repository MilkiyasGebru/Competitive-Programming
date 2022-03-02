class Solution:
    def maxDepth(self, root: 'Node') -> int:                
        def depthFinder(root):
            if len(root.children)==0:
                return 1
            else:
                depth=0
                for i in root.children:
                    depth=max(depth, 1 + depthFinder(i)) 
                return depth
        if root==None:
            return 0
        return depthFinder(root)
