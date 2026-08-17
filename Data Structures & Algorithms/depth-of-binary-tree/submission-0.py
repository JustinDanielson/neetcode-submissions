# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depthCount(root: Optional[TreeNode], height = 0):
            if root:
                return max(
                    depthCount(root.left, height + 1), 
                    depthCount(root.right, height + 1)
                )
            return height
        return depthCount(root, 0)