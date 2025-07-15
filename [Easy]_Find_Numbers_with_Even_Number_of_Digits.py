class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            dig_count = 0
            temp = num

            while temp != 0:
                temp = temp // 10
                dig_count += 1

            if dig_count % 2 == 0:
                count += 1

        return count
