# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def pre_order(node):
            if not node:
                # important to yield NONE if there is no node before returning
                yield None
                return
            yield node.val
            yield from pre_order(node.left)
            yield from pre_order(node.right)

        for a,b in zip(pre_order(p), pre_order(q)):
            if a != b:
                return False
        return True