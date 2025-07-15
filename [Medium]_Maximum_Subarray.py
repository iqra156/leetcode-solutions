class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        start = end = temp_start = 0

        for i in range (1, len(nums)):
            num = nums[i]

            if num > current_sum + num:
                current_sum = num
                temp_start = i

            else:
                current_sum += num

            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i

        return max_sum
