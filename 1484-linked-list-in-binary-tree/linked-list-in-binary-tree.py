# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isTrue(head1, root1):
            if head1 is None:  # If the linked list is completely traversed, it's a match
                return True
            if root1 is None:  # If the tree node is None and list still has elements, no match
                return False
            if head1.val != root1.val:  # Values don't match
                return False
            # Recur on left and right subtrees
            return isTrue(head1.next, root1.left) or isTrue(head1.next, root1.right)

        def dfs(root):
            if root is None:  # Base case: if root is null, we can't check further
                return False
            # If a match is found starting at this node, return True
            if isTrue(head, root):
                return True
            # Continue DFS on left and right children
            return dfs(root.left) or dfs(root.right)

        return dfs(root)
