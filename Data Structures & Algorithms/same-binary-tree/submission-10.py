# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def doubleDfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p and q:
                return p.val == q.val and \
                    doubleDfs(p.left, q.left) and doubleDfs(p.right, q.right)
            elif not p and not q:
                return True
            else:
                return False
        return doubleDfs(p, q)
