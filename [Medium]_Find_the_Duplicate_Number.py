class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                return num


                
# I am given a list of numbers where each number is between 1 and n, but the list has n + 1 numbers. That means one number is definitely repeated. My task is to find which number is repeated. However, I’m not allowed to change the list in any way, and I can’t use extra memory like new arrays or hash maps. I have to find the duplicate using only a small, fixed amount of extra space.