class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}  # dict
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in d:
                return [i, d[temp]]
            d[nums[i]] = i