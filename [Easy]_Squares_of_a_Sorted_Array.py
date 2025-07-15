class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left]**2
                left += 1 
            else:
                result[pos] = nums[right]**2
                right -= 1
            pos -= 1

        return result


# Ham ne phle len array ki find ki aur variable mei dali q k jitni array ki len ho gi ham new array utnay size ki bnaei gei aur initially 0 store krwa dein ge. left pointer index 0 pe hai right pointer end wale index pe hai. ham position variable lein gei es me har iteration me change aye ga q k ham har iteration pe result array mein kuch na kuch store karein gei squre kar k. pos variable end index se start o ga q k max squre result k end pe ho gi tu hamein extra sort nhi krna pre ga. while loop chlaein ge jab tak dono pointers cross nhi krte.left aur right ddono ki values compare karein gei agar left ki bar hai tu uska squre lei k result ki current position pe store krwa dein gei nhi tu right ki. ab result ka last index fill ho gea hai ham 2nd last pe ayein gein mtlab decrement ho ga. Aur left aur right mein se wo increment ya decrement ho ga jo jiski abs value bari nikli thi. aur end pe ham result array return krwa dein gei
