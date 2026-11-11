class Solution:

# Pass in our string into one giant string list at a time 
# and use the other function to print out our orginal list again

# we can't just encode / pass in 'c' 'a' 't' 
# because our other function (decode) 
# won't recognize what is going on to decode it pass it back to
# our orginal code

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res