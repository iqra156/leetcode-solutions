class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        
        for i in range (1, len(nums)):
            if nums[i] != nums[i-1]:
              nums[k] = nums[i]
              k += 1
        return k

        # k aik pointer variable hai jo k index 0 pe pra hai mtlab unique element ki jo array ham return karein gei uska 1st element always unique ho ga. esi liye ham array traverse index 1 se start krte hain. agar array khali hai 0 return kar do. agar nhi khali usko traverse karo i pointer k through i start ho ga 1 se jo k index 1 hai . index i ko indexi-1 se compare krna hai agar doo same nhi hain eska mtlab hai i index wala unique hai usko k mein dalo aur k ka count brha do. agar same hain tu kuch b nhi krna end pe k wapis kr dena hai.