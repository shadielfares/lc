class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #add every number from 1st list to hashset, and then check for every num in 2nd list
        #if its in hashset then remove it and append to solution
        solution = []
        hashset = set(nums1) #{1,2}

        for num in nums2: #[2,2]
            if num in hashset:
                hashset.remove(num)
                solution.append(num)
        print(solution)
        return solution
            

