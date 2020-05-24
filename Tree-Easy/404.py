# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(rootL, rootR):

            if rootL:
                if not rootL.left and not rootL.right:

                    self.res += rootL.val
                else:
                    helper(rootL.left, rootL.right)
            if rootR:
                helper(rootR.left, rootR.right)

        self.res = 0
        if root:

            if root.left or root.right:
                helper(root.left, root.right)

        return self.res

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)