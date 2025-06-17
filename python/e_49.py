class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Use a hashmap
        #Keys: sortedWord
        #Val: Array of anagrams
        results = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            results[sortedWord].append(word)

        return list(results.values())