# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node, s):
            if not node:
                return 0
            if not node.right and not node.left:
                return s
            return max(helper(node.left, s + 1), helper(node.right, s + 1))

        return helper(root, 1)
