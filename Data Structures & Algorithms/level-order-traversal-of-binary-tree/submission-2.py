# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # Implemented using a deque bc list.pop removes last element, not first.
        # list pop resulted in [[1],[2,3],[6,7,4,5]] because 3 was popped before 2
        # list comprehension on res.append(...) goes left to right
        # that's why [2,3] were in order
        q = deque([root])
        res = list()
        while q:
            res.append([n.val for n in q])
            next_level = deque()
            while q:
                node = q.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            q = next_level
        return res