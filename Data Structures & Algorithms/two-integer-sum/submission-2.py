class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            # {0; 4, 1; 5, 2: 6}
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i

            # need to return the index position 
            
