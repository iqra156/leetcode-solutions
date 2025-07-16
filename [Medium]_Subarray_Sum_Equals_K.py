class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0  # Total number of subarrays found
        total = 0  # Running sum (prefix sum)
        prefix_sums = {
            0: 1
        }  # Stores count of each prefix sum mean 0 sum is seen one time

        for num in nums:
            total += num  # Add current number to running total

            # Check if there's a subarray that sums to k
            if total - k in prefix_sums:
                count += prefix_sums[total - k]

            # Update the prefix_sums dictionary
            prefix_sums[total] = prefix_sums.get(total, 0) + 1

        return count
