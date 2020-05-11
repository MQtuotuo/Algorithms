# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []
        output = []
        if root is None:
            return None
        queue.append(root)

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level)
        return reversed(output)

    def levelOrderBottom_r(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ret = deque()

        def fn(node, depth):
            if len(ret) < depth:
                ret.appendleft([])

            ret[-depth].append(node.val)
            if node.left: fn(node.left, depth + 1)
            if node.right: fn(node.right, depth + 1)

        fn(root, 1)
        return ret
