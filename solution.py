# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Val, l2Val = "", ""
        while l1 or l2:
            if l1:
                l1Val += str(l1.val)
                l1 = l1.next
            if l2:
                l2Val += str(l2.val)
                l2 = l2.next
        
        resVal = str( int(l1Val[::-1]) + int(l2Val[::-1]) )[::-1]
                
        res = ListNode(int(resVal[0]))
        tempNode = res

        for digit in resVal[1:]:
            tempNode.next = ListNode(int(digit))
            tempNode = tempNode.next
        
        return res
