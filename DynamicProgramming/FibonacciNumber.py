f = {}
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else :
            if n-1 not in f:
                f[n-1]=self.fib(n-1)
            if n-2 not in f:
                f[n-2]=self.fib(n-2)
            return f[n-1] + f[n-2]
        
