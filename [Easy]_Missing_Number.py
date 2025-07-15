class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}

        for num in nums:
            freq[num] = True

        for i in range(n + 1):
            if i not in freq:
                return i
