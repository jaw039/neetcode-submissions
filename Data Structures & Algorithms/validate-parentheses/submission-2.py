class Solution:
    def isValid(self, s: str) -> bool:
        # create an empty stack 
        st = []
        # add each brackets into stack (st) if it is there
        # first comes in the opening bracket
        for c in s:
            if c == '[' or c == '{' or c == '(':
                st.append(c)
        # now check the opposite end of it to see if is right
        # last comes out the closing bracket
            elif c == ')' or c == '}' or c == ']':
                if not st:
                    return False

                top = st[-1]
                if ((c == ')' and top != '(') or
                    (c == '}' and top != '{') or
                    (c == ']' and top != '[')):
                    return False
                
                st.pop()
        return not st





            
                