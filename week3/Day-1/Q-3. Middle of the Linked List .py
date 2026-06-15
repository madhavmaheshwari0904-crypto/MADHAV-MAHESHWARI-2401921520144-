# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n=0
        temp=head
        while(temp!=None):
            n+=1
            temp=temp.next
        temp=head
        i=0    
        while(i<n//2):
            temp=temp.next
            i+=1
        head=temp
        return head