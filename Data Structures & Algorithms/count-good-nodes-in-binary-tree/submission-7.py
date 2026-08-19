# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursively pass down val = max(node.val, max_val)
    def goodNodes(self, root: TreeNode) -> int:
        #result = []
        goodNodeCount = 0
        def dfs(node: TreeNode, max_val=float("-INF")):
            if node:
                if node.val >= max_val:
                    #result.append(node.val)
                    nonlocal goodNodeCount
                    goodNodeCount += 1
                    max_val = node.val
                dfs(node.right, max_val)
                dfs(node.left, max_val)
        dfs(root)
        #return len(result)
        return goodNodeCount

        