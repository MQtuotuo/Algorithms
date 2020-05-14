# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def rec(nums, start, end):
            if start <= end:
                mid = (start + end) // 2
                node = TreeNode(nums[mid])
                node.left = rec(nums, start, mid - 1)
                node.right = rec(nums, mid + 1, end)
                return node
        return rec(nums, 0, len(nums) - 1)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if len(nums) == 0:
            # Base case: ( also known as stop condtion )
            return None

        else:
            # General case:
            # Solve by divide-and-conquer

            # conquer
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            # divide
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])

            return root