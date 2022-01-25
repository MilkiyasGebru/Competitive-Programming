# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        header = head
        stack=[]
        if(head==None):
            return head
        while(header):
            stack.append(header.val)
            header = header.next
        stack.sort()
        header = head
        for i in range(len(stack)):
            header.val = stack[i]
            header = header.next
        return head    
            
