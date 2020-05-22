# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree_i(self, root: TreeNode) -> TreeNode:
        if root == None: return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return root


    def invertTree_r(self, root: TreeNode) -> TreeNode:

        def rec(root):
            if root:
                root.left, root.right = root.right, root.left
                rec(root.left)
                rec(root.right)

        rec(root)
        return root