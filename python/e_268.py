class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numRange = [x for x in range(len(nums) + 1)]
        for num in nums:
            if num in numRange:
                numRange.remove(num)
        return numRange[0]