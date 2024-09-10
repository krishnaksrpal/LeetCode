# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        first = head
        second= head.next
        while(second != None):
            ins = math.gcd(first.val,second.val)
            first.next = ListNode(ins,second)
            second = second.next
            first = first.next.next
        return head
