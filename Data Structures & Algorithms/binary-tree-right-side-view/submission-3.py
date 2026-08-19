# Definition for a binary tree node.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def post_order(root: Optional[TreeNode], level = 1): 
            if not root:
                return
            nonlocal result
            if len(result) < level:
                result.append(root.val)
            post_order(root.right, level + 1)
            post_order(root.left, level + 1)
        post_order(root)
        return result