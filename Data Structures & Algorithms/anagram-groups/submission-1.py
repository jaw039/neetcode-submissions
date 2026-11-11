class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # signature -> list of words
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)          # lists can't be dict keys, tuples can
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())