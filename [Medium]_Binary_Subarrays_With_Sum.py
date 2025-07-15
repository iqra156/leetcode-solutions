from collections import defaultdict  # Import at the top of the file

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0  # This will store the running total (sum from start to current index)
        count = 0       # This will count how many valid subarrays we find
        freq = defaultdict(int)  # Stores how many times each prefix sum has occurred
        freq[0] = 1  # Handle the case where a subarray from index 0 has a sum equal to goal

        # Loop through each number in the array
        for num in nums:
            prefix_sum += num  # Update running total

            # Check if we have seen a prefix_sum such that current_sum - previous_sum = goal
            count += freq[prefix_sum - goal]  # If yes, add how many times it occurred

            # Record that we've seen this prefix_sum one more time
            freq[prefix_sum] += 1

        return count  # Return total number of valid subarrays
