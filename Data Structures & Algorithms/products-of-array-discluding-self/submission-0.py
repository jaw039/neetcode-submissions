class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        # Get the target index -> which index do we need to ignore  (outer loop)
        for i in range(len(nums)):
            current_product = 1
            # Make sure that the target index number doesn't get included when multiplying 
            for j in range(len(nums)):
                if i != j:
                    current_product = current_product * nums[j]
            output.append(current_product)
        return output