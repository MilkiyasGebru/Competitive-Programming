class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.Times = times
        f={}
        self.arr=[]
        
        index = 0
        count = 0
        
        while(index < len(times)):
            
            if persons[index] not in f:
                f[persons[index]]=1
                
                if f[persons[index]] >= count:
                    count = f[persons[index]]
                    
                    self.arr.append(persons[index])
                    
                else:
                    self.arr.append(self.arr[index-1])
            else:
                
                f[persons[index]]+=1
                
                if f[persons[index]] >= count:
                    
                    count = f[persons[index]]
                    self.arr.append(persons[index])
                    
                else:
                    self.arr.append(self.arr[index-1])
            index += 1        
                
            
    def q(self, t: int) -> int:
        
        left = 0
        right = len(self.Times)-1
        ans = left
        
        while(left<=right):
            
            mid = (left + right)//2
            
            if self.Times[mid] > t:
                right = mid - 1
                
            else:
                ans = mid 
                left = mid + 1
                
        
        return self.arr[ans] 
