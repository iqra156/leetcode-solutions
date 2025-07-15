class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for key, value in freq.items():
            if value > len(nums) // 2:
                return key
