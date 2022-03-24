class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
       
        def answer(k,i):
            if k==1  :
                return "0",i
            elif k==2:
                return "1",i
            else:
                x = int(math.log2(k))
                x = 2**(x)
                if  k - int(x)==0 :
                    return answer(k//2,-i)
                return answer(k-int(x),-i)
         
        a,b = answer(k,1)
        if b==1:
            return a
        else:
            if a =="0":
                return "1"
            else:
                return "0"

        
