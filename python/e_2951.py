class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        # Mountain.length is 3 or greater always
        #I can use a two-pointer soln to check if the index to the right of right pointer is less than the left
        l = 0
        soln = []
        while l < len(mountain) - 2:
            r = l + 1
            if mountain[l] < mountain[r] and mountain[r] > mountain[r+1]:
                soln.append(r)
            l += 1
        return soln