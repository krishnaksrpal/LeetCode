# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        curr = head
        while top <= bottom and left <= right and curr:
            for i in range(left, right + 1):
                if curr:
                    matrix[top][i] = curr.val
                    curr = curr.next
            top += 1
            for i in range(top, bottom + 1):
                if curr:
                    matrix[i][right] = curr.val
                    curr = curr.next
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    if curr:
                        matrix[bottom][i] = curr.val
                        curr = curr.next
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if curr:
                        matrix[i][left] = curr.val
                        curr = curr.next
                left += 1
        return matrix