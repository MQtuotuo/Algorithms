# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            # empty node
            return False

        else:
            if root.val == sum and root.left is None and root.right is None:
                # leaf node
                return True

            else:

                # non-leaf node
                has_left_path = self.hasPathSum(root.left, sum - root.val)
                has_right_path = self.hasPathSum(root.right, sum - root.val)

                return has_left_path or has_right_path

    def hasPathSum_dfs(self, root: TreeNode, sum: int) -> bool:
        traversal_stack = [(root, sum)]

        # DFS with stack
        while traversal_stack:

            node, value = traversal_stack.pop()

            if node:
                if node.left == None and node.right == None and node.val == value:
                    # leaf node
                    return True

                else:
                    # non-leaf node
                    traversal_stack.append((node.right, value - node.val))
                    traversal_stack.append((node.left, value - node.val))

            else:
                # empty node
                continue

        return False
