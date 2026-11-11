class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # only keeps the unique element in the nums list to the hash set 
        numSet = set(nums)

        # initialize our longest sequence first to be 0
        longest = 0

        # iterate the new list
        for n in nums:
            # if 2 - 1 not in NumSet -> set our length to 0 
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


