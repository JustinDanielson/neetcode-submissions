# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = list()
        while q:
            res.append([n.val for n in q])
            next_level = list()
            while q:
                node = q.pop(0) # FIFO for left to right level traversal
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            q = next_level
        return res