# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def calcHeight(root: Optional[TreeNode], height = 1) -> int:
            if root:
                left = calcHeight(root.left, height + 1) if root.left else 0
                right = calcHeight(root.right, height + 1) if root.right else 0
            return max(height, left, right)
        queue = [root]
        while queue:
            node = queue.pop()
            left = right = 0
            if node.left:
                left = calcHeight(node.left)
                queue.append(node.left)
            if node.right:
                right = calcHeight(node.right)
                queue.append(node.right)
            diameter = max(diameter, left + right)
        return diameter