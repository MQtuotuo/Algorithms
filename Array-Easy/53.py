class Solution:
    def maxSubArray(self, nums) -> int:
        maxcurr = nums[0]
        maxglobal = nums[0]
        for i in range(1,len(nums)):
            maxcurr = max(nums[i], maxcurr + nums[i])
            maxglobal = max(maxcurr, maxglobal)
            print(maxcurr)
            print(maxglobal)
        return maxglobal

ep = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
rs = s.maxSubArray(ep)
print(rs)