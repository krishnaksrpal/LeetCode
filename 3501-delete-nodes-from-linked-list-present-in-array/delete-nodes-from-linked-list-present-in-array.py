# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        set_nums = set(nums)
        while (head != None and head.val in set_nums):
            head = head.next
        temp = head
        while temp != None and temp.next != None:
            if temp.next.val in set_nums:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head