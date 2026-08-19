# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(a: TreeNode, b: TreeNode) -> bool:
            if a and b and a.val == b.val:
                return equal(a.left, b.left) and equal(a.right, b.right)
            elif not a and not b:
                return True
            else:
                return False

        def find(root: Optional[TreeNode], val: int) -> TreeNode:
            if root:
                if root.val == val:
                    yield root
                yield from find(root.left, val)
                yield from find(root.right, val)

        for r in find(root, subRoot.val):
            if equal(r, subRoot):
                return True
        return False