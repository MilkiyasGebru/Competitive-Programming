class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum=0
        def finder(root,parent=None,grand=None):
            if root==None:
                return
            else:
                if grand and grand.val%2==0:
                    nonlocal sum
                    sum += root.val
                finder(root.left,root,parent)
                finder(root.right,root,parent)
                
              
        finder(root)
        return sum
      
 class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum=0
        even=[0]*1000
        def finder(root,height,even):
            if root == None :
                return 0
            else: 
                even[height]=root.val
                if height >=2 and even[height-2]%2==0:
                    nonlocal sum

                    sum +=root.val
                
                finder(root.left,height+1,even)
                finder(root.right,height+1,even)
                
        finder(root,0,even)
        return sum
