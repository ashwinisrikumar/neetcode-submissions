# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n>0:
            right = right.next
            n= n-1

        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next






        """
        dummy -> 1 -> 
        1,2,3,4
        2 1 0
        L   R
          L   R
             

        3 from theend
        n - 3 from beginning -> 8 - 3 = 5
        1,2,3,4,5,6,7,8
        R
          R
            R
        L   R
          L    R
                L    R


        """
        