class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_set = set(nums)
        longest_sequence = 0
        current_sequence = 0

        print(sorted_set)
        for num in sorted_set:
            if num - 1 not in sorted_set:
                current_num = num
                current_sequence = 1
            
                while current_num + 1 in sorted_set:
                    current_sequence += 1
                    current_num += 1

            longest_sequence = max(longest_sequence, current_sequence)
        return longest_sequence