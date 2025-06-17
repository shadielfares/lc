class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Criteria for finding a unique character
        # It must be unique, so it must exist in the hashmap
        # After existing in the hashmap,
        hm = {}
        unique_chars = []
        non_unique = []
        for i in range(len(s)):
            if s[i] not in hm and s[i] not in non_unique:
                hm[s[i]] = i
            else:
                if s[i] not in non_unique:
                    non_unique.append(s[i])
            
        soln  = []
        for key, value in hm.items():
            if key not in non_unique:
                soln.append([key, value])

        if len(soln) > 0:
            return soln[0][1]
        else:
            return -1