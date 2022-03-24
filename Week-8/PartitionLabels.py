class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer=[]
        f={}
        for i in range(len(s)):
            f[s[i]]=i
        i=0
        first=0
        last=0
        while(i<len(s)):
            if i <= last and i < len(s)-1:
                last = max(last,f[s[i]])
            else:
                answer.append(last-first+1)
                if i == len(s)-1 and last == len(s)-1:
                    break
                first=last=i    
                continue
            i=i+1   
        return answer    
                
