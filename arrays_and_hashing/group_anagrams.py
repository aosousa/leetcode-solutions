class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            
            anagrams[sorted_s].append(s)
        
        return anagrams.values()