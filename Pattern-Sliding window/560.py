def subarraySum(self, nums: List[int], k: int) -> int:
	 if len(nums) == 1:
		 if nums[0] == k:
			 return 1
		 else:
			 return 0

	 # O(n) solution
	 count = 0
	 i, j = 0, 1
	 s = nums[i:j+1]
	 while j < len(nums):
		 if s == k:       # --- increment count and then disturbe the window again
			 count += 1
			 j += 1 # disturbacne
		 elif s < target:   # --- expand window - if sum goes beyond target - it will go to the else and window will shrink again
			j += 1
			s += nums[j]
		else:
			# shrink
			s -= nums[i]
			i += 1

	 return count