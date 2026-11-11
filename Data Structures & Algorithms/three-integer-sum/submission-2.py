class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # results = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 results.append([nums[i], nums[j], nums[k]])
        # return results

        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i + 1, n-1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i],nums[lo],nums[hi]])
                    lo,hi = lo+1, hi-1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1
        return answer