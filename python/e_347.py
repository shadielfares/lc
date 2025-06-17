class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        array = []
        for key, count in hashmap.items():
            array.append([count, key])
        array.sort()
        
        result =[]

        while len(result) < k:
            result.append(array.pop()[1])
        
        return result