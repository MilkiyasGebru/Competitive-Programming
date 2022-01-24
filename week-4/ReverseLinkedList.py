class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        y = None
        header = head
        if head==None:
            return head
        else:
            head = self.reverser(header,y)
        return head
    def reverser(self,head,y):
        x = head.next
        head.next = y
        y = head
        
        if (x == None):
            return y
        else :
            return self.reverser(x,y)
