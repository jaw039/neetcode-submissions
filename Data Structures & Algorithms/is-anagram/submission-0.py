class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_string1 = ''.join(sorted(s))
        sorted_string2 = ''.join(sorted(t))
        if sorted_string1 == sorted_string2:
            return True
        else: 
            return False