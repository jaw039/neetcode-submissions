# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # so the the tree has to go from smallest to largest cannot be larger
        # use post order depth first search 

        # 1. Use DFS in left → current → right order.
        # 2. When you reach an empty node, return from that branch—this is your base case.
        # 3. When processing the current node:
        #    - If it’s the first value visited, skip the comparison.
        #    - Otherwise, check that it’s strictly greater than the previous value. If it isn’t, the tree is invalid.
        #    - Remember the current value as your new previous value.
        # 4. Continue into the right subtree.
        # 5. Return true only if the whole traversal finishes without a violation.
        # For example, visiting 1 → 2 → 3 passes. Visiting 1 → 5 → 3 fails when you reach 3, because 3 is smaller than 5.
        stack = []
        current = root
        previous = None

        while current is not None or stack:
            # Go as far left as possible.
            while current is not None:
                stack.append(current)
                current = current.left

            # Process the next node in inorder.
            current = stack.pop()

            if previous is not None and current.val <= previous:
                return False

            previous = current.val

            # Explore the right subtree next.
            current = current.right

        return True