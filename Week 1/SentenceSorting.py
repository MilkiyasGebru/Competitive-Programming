class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        b=""
        x = len(a)
        for i in range(0,x):
            for j in range(0, x):
                if j < x - 1 and a[j][-1] > a[j + 1][-1]:
                    c = a[j + 1]
                    a[j + 1] = a[j]
                    a[j] = c
        for i in range(0,x):
            a[i]=a[i].replace(a[i][-1],"")
        b=a[0]    
        if x>1 :
            for j in range(1,x):
                b=b+" "+a[j]
        return b    
