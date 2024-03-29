# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.res = []
        self.dfs(root, str(root.val))
        return self.res

    def dfs(self, root, path):
        if not root.left and not root.right:
            self.res.append(path)
        if root.left:
            self.dfs(root.left, path + "->" + str(root.left.val))
        if root.right:
            self.dfs(root.right, path + "->" + str(root.right.val))

    def binaryTreePaths_i(self, root):
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node:
                continue
            if not node.left and not node.right:
                res.append("{}{}".format(path, node.val))
            stack.append((node.left, "{}{}->".format(path, node.val)))
            stack.append((node.right, "{}{}->".format(path, node.val)))
        return res
