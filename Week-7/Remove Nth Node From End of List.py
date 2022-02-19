class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        header=head
        while(header):
            count +=1
            header=header.next
        if(count==1):
            return None
        elif(count==n):
            head = head.next
            return head
        else:
            count-=n+1
            header=head
            while(not count==0):
                header=header.next
                count-=1
            header.next=header.next.next
            return head
