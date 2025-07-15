class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        # at each index we will find the max and min because in product both positive and negative number effect greatly the product

        for num in nums[1:]:
            temp_max = max(num, current_max * num, current_min * num)
            current_min = min(num, current_max * num, current_min * num)
            current_max = temp_max

            # we use temp cuz we wil use value of current max to calculate min if we directly add max value in current max,it is updated and updated value will be used in next line which is not correct

            max_product = max(max_product, current_max)
        # max-product will be calculated by max product untill now and last calculated product current-max

        return max_product
