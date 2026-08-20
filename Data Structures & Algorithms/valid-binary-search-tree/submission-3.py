# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Need to traverse tree and pass to child nodes
# min, max that bound the values that can exist within the subtrees
# If you're going left, you have a new max
# If you're going right, you have a new min
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_bst_valid(root: TreeNode, lo = float("-INF"), hi = float("INF")) -> bool:
            if not root:
                return True
            return lo < root.val < hi and \
                is_bst_valid(root.left, lo, root.val) and \
                is_bst_valid(root.right, root.val, hi)
        return is_bst_valid(root)