class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # continue iterating until we get the target 

        # create the left pointer, right pointer 
        left = 0
        right = len(numbers) - 1

        # add them up together to see if they equal to target
        while left < right:
            total = numbers[left] + numbers[right]

        # if they equal target print the output
            if total == target:
                # we add the index by 1 because array starts counting at 0 and for us to get the correct position of the array for the user we have to add 1 
                return [left + 1, right + 1]

        # if the target is bigger, move the right pointer to the left, as this is non increasing order, if we move the left pointer our target will only keep increasing, but if we move the right pointer our target value will be smaller 
            elif total > target:
                right -= 1 

            elif total < target:
                left += 1 

            

        