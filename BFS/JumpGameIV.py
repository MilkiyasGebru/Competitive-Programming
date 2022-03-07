
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        nums={}
        steps=0
        direction=[-1,1]
        queue = deque([0])
        visited = set()
        visited.add(0)
        
        def bound(i):
            
            return 0 <= i < len(arr)   and not i in visited
        
        
        for i in range(len(arr)):
            
            nums[arr[i]] = i

                
        def checker(i):
            
            for j in direction:
                
                inew = i + j
                
                if bound(inew):
                    queue.append(inew)
                    visited.add(inew)
                    
            val = nums[arr[i]]    
            
            if not val in visited:
                queue.append(val)
                visited.add(val)
            
        while(queue and not len(arr)-1 in visited ):
            
            steps +=1
            valid = len(queue)
            
            while(valid > 0):
                
                valid -=1
                header = queue.popleft()
                checker(header)
                
        return steps        
                
                
                
