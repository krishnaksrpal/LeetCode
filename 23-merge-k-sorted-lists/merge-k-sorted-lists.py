# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        def findMinVal():
            
            mini = 10_000_000_000
            index = 0
            for i in range(n):
                lis = lists[i]
                if lis == None:
                    continue
                if mini > lis.val:
                    mini = lis.val
                    index = i
            lists[index] = lists[index].next
            return mini

        def empty():
            for lis in lists:
                if lis is not None:
                    return False
            return True
        
        ans = ListNode()
        temp = ans
        while(not empty()):
            minimum_val = findMinVal()
            temp.next = ListNode(val = minimum_val)
            temp = temp.next
        return ans.next


