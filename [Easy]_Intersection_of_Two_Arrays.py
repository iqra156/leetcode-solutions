class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        result = set()

        for i in nums1:
            freq[i] = True  # Store all nums1 values in a dictionary

        for i in nums2:
            if i in freq:   # If nums2 value is in nums1
                result.add(i)  # Add to result set (unique only)

        return list(result)  # Convert set to list before returning
