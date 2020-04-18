
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                print(j)
                nums[j] = nums[i]
                print(nums)
                j=j+1
        for i in range(len(nums)-j):
            nums.pop()

nums = [0,1,2,2,3,0,4,2]
val = 2

s = Solution()
s.removeElement(nums, val)