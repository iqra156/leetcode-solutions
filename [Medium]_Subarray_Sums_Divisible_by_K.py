class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        prefix_mod = {0: 1}  # base case: mod 0 seen once

        for num in nums:
            total += num
            mod = total % k  # Use total, not just num

            # Handle negative mods correctly
            if mod < 0:
                mod += k

            # Add the frequency of this mod to the count
            count += prefix_mod.get(mod, 0)

            # Update the prefix_mod dictionary
            prefix_mod[mod] = prefix_mod.get(mod, 0) + 1

        return count
