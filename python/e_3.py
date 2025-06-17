class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        l, maxLen = 0, 0
        for r in range(n):
            if s[r] not in char_set:
                char_set.add(s[r])
                maxLen = max(maxLen, r - l + 1)
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
                char_set.add(s[r])
        return maxLen