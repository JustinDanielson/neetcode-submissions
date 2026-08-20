# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def inorder_kth(node: TreeNode, k, count = 0):
            if node:
                print(node.val)
            nonlocal res
            if res != None:
                return -1
            # Count left side of tree
            if res == None and node.left:
                count = inorder_kth(node.left, k, count)
            # Count self
            count += 1
            if res == None and count == k:
                res = node.val
                return -1
            # Visit right and send count down
            if res == None and node.right:
                count = inorder_kth(node.right, k, count)
            return count
        inorder_kth(root, k)
        return res