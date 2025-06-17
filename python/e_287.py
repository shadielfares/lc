class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Notes:

        Can' we keep a variable to compare and instantly solve it in O(n^2) time complexity

        By keeping one variable, it is constant for all solns
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        