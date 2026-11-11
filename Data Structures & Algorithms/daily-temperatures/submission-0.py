class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)   
        # i = today's index
        # temp = today's temperature
        for i, temp in enumerate(temperatures):
            # use stack to remember that days temp to compare future days temp
            # 0, 30 ; 1; 38
            # you now want to check when is the next day the temperture will be higher
            while stack and temp > temperatures[stack[-1]]:
                past_day = stack.pop()
                results[past_day] = i - past_day

            stack.append(i)
        return results
