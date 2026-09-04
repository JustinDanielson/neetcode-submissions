# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder_iterator(self, root: Optional[TreeNode]) -> TreeNode:
        if not root: return
        yield from self.inorder_iterator(root.left)
        yield root
        yield from self.inorder_iterator(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k:int) -> int:
        res = None
        for res in self.inorder_iterator(root):
            k -= 1
            if k == 0: return res.val
 
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # This solution returns early if the result is already known
    #     res = None
    #     def inorder_kth(node: TreeNode, k, count = 0):
    #         if node:
    #             print(node.val)
    #         nonlocal res
    #         if res != None:
    #             return -1
    #         # Count left side of tree
    #         if res == None and node.left:
    #             count = inorder_kth(node.left, k, count)
    #         # Count self
    #         count += 1
    #         if res == None and count == k:
    #             res = node.val
    #             return -1
    #         # Visit right and send count down
    #         if res == None and node.right:
    #             count = inorder_kth(node.right, k, count)
    #         return count
    #     inorder_kth(root, k)
    #     return res

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # This solution is faster to implement, but it doesn't return early
    #     # It searches the entire tree.
    #     res = None
    #     def inorder_kth(node: Optional[TreeNode], k, count = 0):
    #         nonlocal res
    #         if not node:
    #             return count
    #         count = inorder_kth(node.left, k, count)
    #         count += 1
    #         if count == k:
    #             res = node.val
    #         count = inorder_kth(node.right, k, count)
    #         return count
    #     inorder_kth(root, k)
    #     return res