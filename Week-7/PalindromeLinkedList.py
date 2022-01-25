# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        header = head
        while(header):
            stack.append(header.val)
            header = header.next    
        for i in range(0,len(stack)//2):
            if stack[i]==stack[len(stack)-i-1]:
                continue
            else:
                return False
        return True    
