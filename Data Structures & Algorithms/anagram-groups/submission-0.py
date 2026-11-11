class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Empty Dictionary serve as a memory bank
        anagramMap = {}
        # 2. Start the loop to grab one word at a time
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagramMap:
                anagramMap[sorted_word].append(word)
            else:
                anagramMap[sorted_word] = [word]
        return list(anagramMap.values())