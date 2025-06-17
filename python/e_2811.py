class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # Can solve this recurrsively
        #Base case is if current array is of length 2 and if each of the items sum to m
        # Current base case is incorrect
        # We actually need to check if the result is equal on every iteration, so we can 
        if len(nums) <= 2:
            return True
        
        for i in range(len(nums) -1):
            if nums[i] + nums[i+1] >= m:
                return True
        
        return False