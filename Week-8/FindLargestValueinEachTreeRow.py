class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
            Q = deque()
            
            if root != None:
                Q.append(root)
                
            answer =[]
            val=-sys.maxsize - 1
            while(Q):
                x = len(Q)
                while(x > 0):
                    node = Q.popleft()
                    val = max(val,node.val)
                    if node.left : Q.append(node.left)
                    if node.right : Q.append(node.right)
                    x-=1
                answer.append(val)    
                val = -sys.maxsize - 1
            return answer  
