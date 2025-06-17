class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        
        occurances = []
        
        for key, value in hm.items():
            occurances.append([key, value])

        occurances.sort(key=lambda x: x[1])
        print(occurances)

        print(occurances[::-1])
        return occurances[::-1][0][0]