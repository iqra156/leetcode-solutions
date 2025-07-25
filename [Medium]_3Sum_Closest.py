from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')  # Store the closest sum found so far

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If the current sum is closer to target, update closest
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # Move pointers based on comparison
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If it's exactly equal, it's the best possible answer
                    return current_sum

        return closest
