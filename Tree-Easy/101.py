# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def dfs(p, q):
            if p==q==None:
                return True
            if (not p) or (not q):
                return False
            if p.val!=q.val:
                return False
            return dfs(p.left, q.right) and dfs(p.right, q.left)
        return dfs(root.left, root.right)

    def isSymmetric_i(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        stack = [(root.left, root.right)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return n1 == n2
            if n1.val != n2.val:
                return False
            stack.append((n1.right, n2.left))
            stack.append((n1.left, n2.right))
        return True