class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            elif nums[mid] >= nums[l]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            # right sorted portion
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1



# # Step 1: Pick the middle and check it.
# If nums[mid] is the target, you’re done. If not, mid is never the answer again, so both pointer moves skip past it (mid + 1 and mid - 1).

# Step 2: Find a sorted half.
# After splitting at mid, the drop (the rotation point) can only be in one half, so the other half has no drop and is sorted. You can tell which by comparing nums[mid] to nums[l]:

# nums[mid] >= nums[l]: no drop between l and mid, so the left half is sorted.
# Otherwise the drop is on the left, so the right half is sorted.

# Step 3: Ask whether the target is inside the sorted half.
# You can only answer that for the sorted half, because for a sorted stretch the endpoints tell you everything. If the target is between the two endpoints, it’s in there. If it’s outside them, it can’t be. You can’t make that claim about the half with the drop, since its endpoints don’t bound what’s inside.

# Step 4: Discard accordingly.

# Target is inside the sorted half: throw away the other half.
# Target is not inside the sorted half: throw away the sorted half, since the target has to be in the other one.

# Which side that is depends on which half was sorted:

# Sorted half	Target inside it	Target not inside it
# Left (l to mid)	r = mid - 1	l = mid + 1
# Right (mid to r)	l = mid + 1	r = mid - 1

# Notice the table is symmetric. Whenever the target is inside the sorted half, you keep that half. Whenever it isn’t, you keep the other one. The pointer direction just follows from which half you’re keeping.