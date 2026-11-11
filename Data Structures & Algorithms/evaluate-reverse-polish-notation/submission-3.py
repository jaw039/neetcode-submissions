class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #stack
        operand = ['+', '-', '*', '/']
        for i in tokens:
            if i in operand:
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    if i == '+':
                        stack.append(val1 + val2)
                    if i == '-':
                        stack.append(val2 - val1)
                    if i == '*':
                        stack.append(val1 * val2)
                    if i == '/':
                        stack.append(int(val2 / val1))
            else:
                stack.append(int(i))

        return stack[0]