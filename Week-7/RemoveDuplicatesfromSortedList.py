# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        header = head
        while(header and header.next):
            if(header.val == header.next.val ):
                header.next= header.next.next
            else:
                header = header.next
        return head        
