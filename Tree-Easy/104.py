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

    def maxDepth_i(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        h = 0
        m = 0
        while len(stack):
            top, h = stack.pop()
            if top.left: stack.append([top.left, h + 1])
            if top.right: stack.append([top.right, h + 1])
            m = max(h, m)
        return m