# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            root1, root2 = stack.pop()

            if (not root1 and root2) or (root1 and not root2):
                return False

            if not root1 and not root2:
                continue

            if root1.val != root2.val:
                return False

            stack.append((root1.left, root2.left))
            stack.append((root1.right, root2.right))

        return True

    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        if p == q == None:
            return True

        if (not p and q) or (p and not q):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)