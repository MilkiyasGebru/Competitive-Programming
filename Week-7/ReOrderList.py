# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        header = head
        stack=deque()
        stack1=[]
        count =0
        while(header):
            stack.append(header.val)
            header = header.next
        for i in range(len(stack)):
            if count==0:
                stack1.append(stack.popleft())
                count=1
            else:
                count=0
                stack1.append(stack.pop())         
        header = head
        for i in range(len(stack1)):
            header.val=stack1[i]
            header=header.next
            
            
            
            
            
