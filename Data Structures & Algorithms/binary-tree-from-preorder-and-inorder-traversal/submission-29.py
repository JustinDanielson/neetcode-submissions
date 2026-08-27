# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# You are given two integer arrays preorder and inorder.
# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals and return its root.
# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

# Output: [1,2,3,null,null,null,4]
class Solution:
    # inorder = left, self, right
    # preorder = self, left, right
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        # This look up table is used to O(1) look up an element in the inorder
        inorder_LUT = {val: i for i,val in enumerate(inorder)}

        # Building the tree only uses the preorder
        def buildTreeRecusrive(start, end):
            if start > end or self.idx >= len(preorder):
                return None
            root = TreeNode(preorder[self.idx], None, None)
            mid = inorder_LUT[root.val]
            self.idx += 1
            # if this is a left child of a right subtree, start will not be 0
            root.left = buildTreeRecusrive(start, mid - 1)
            root.right = buildTreeRecusrive(mid + 1, end)
            return root

        return buildTreeRecusrive(0, len(preorder) - 1)


