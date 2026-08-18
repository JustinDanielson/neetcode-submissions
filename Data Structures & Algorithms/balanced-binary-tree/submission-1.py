# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal balanced
            if not root or not balanced:
                return 0
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            if not (-1 <= left - right <= 1):
                balanced = False
            return max(left, right)
        dfs(root)
        return balanced