class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target>nums[i] and target<nums[i+1]:
                return i+1

    def searchInsert1(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

    def searchInsertBS(self, nums, target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

ep = [1,3,5,6]
target = 0
s = Solution()
rs = s.searchInsertBS(ep, target)
print(rs)