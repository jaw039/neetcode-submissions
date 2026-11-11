class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        last = nums[-1]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > last:
                left = mid + 1
            else:
                right = mid

        return nums[left]