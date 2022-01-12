class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        x= self.nString(n)
        return x[k-1]
    def invert(self,s):
        z=""
        for i in range(len(s)):
            if s[i]=="0":
                z += "1"
            else:
                z+="0"
        return z        
    def nString(self,i):
        if i==1 :
            return "0"
        else:
            strr = self.nString(i-1)
            return strr + "1" + (self.invert(strr))[::-1]
            
