class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """ 
        numbers = []
        for x in range(1,n+1):
            if x%3==0 and x%5==0 :
                numbers.append("FizzBuzz")
            elif x%3==0 :
                numbers.append("Fizz")
            elif x%5==0 :
                numbers.append("Buzz")
            else :
                
                numbers.append(str(x))
        return numbers 
