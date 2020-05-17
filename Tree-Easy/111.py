# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth_dfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        minDepth = sys.maxsize

        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                minDepth = min(depth, minDepth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return minDepth

    def minDepth_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = Queue()
        queue.put(root)
        level = 0

        while queue:
            count = len(queue)
            level += 1
            while count:
                temp = queue.popleft()
                if temp.left is None and temp.right is None:
                    return level
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                count -= 1
        return level


