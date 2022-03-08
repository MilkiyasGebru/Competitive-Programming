class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome)==1:
            return ""
        
        compare = "a"*(len(palindrome)//2)
        
        pal = palindrome[0:len(palindrome)//2 ]
        
        
        if pal == compare:
            
            return palindrome[0:len(palindrome)-1] + "b"
        
        else:
            i=0
            while(pal[i] == "a"):
                
                i += 1
            return pal[0:i]+"a"+palindrome[i+1:]    
            
            
                
                  
            
