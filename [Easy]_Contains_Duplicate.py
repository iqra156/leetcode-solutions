class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in nums:
            seen[i] = seen.get(i, 0) + 1
            if seen[i] > 1:
                return True  # If any number appears more than once

        return False  # No duplicates found after checking all
