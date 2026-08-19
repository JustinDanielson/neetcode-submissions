# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low_val = min(p.val, q.val)
        hi_val = max(p.val, q.val)
        cur = root
        while cur:     
            if cur.val > hi_val:
                cur = cur.left
            elif cur.val < low_val:
                cur = cur.right
            else:
                return cur