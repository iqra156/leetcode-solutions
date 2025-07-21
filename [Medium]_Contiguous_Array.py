class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_len = 0
        prefix_map = {0:-1}

        for i, num in enumerate(nums):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in prefix_map:
                len = i -  prefix_map[prefix_sum]
                max_len = max(max_len, len)
            else:
                prefix_map[prefix_sum] = i
        
        return max_len

# Ham ne 3 variables liye max_len = sab se bari subarray count krne k liye jo balance hai, prefix_sum= har index pe ab tak ka cumulative sum store krne k liye, prefix_map q k map hai tu ye prefix sum ka phla index store karei ga. Esay -1 rkha gea haitakay array 0 se start ho ham check kar skein k balanced hai k nhi. 1 loop chlae throghout array agar idex pe 0 hai usko -1 kr do agar zero nhi usay plus krdo prefix sum k.Ab dekho jo prefix sum aaya hai wo phle dekha gea hai agar phle b ye seen kia gea hai map tu len ho jae gi 1st index after started index to i tak mtlab jidhar phle dekha tha uske aglay index se le kar i index tak k elements balanced array hai. Ab max length update karo k ab tak jo max thi pichle index pe us mein se aur current index pe jo max len haiun me jo max hai wo max_len me daal do. Agar seen before nhi hua tu i ko simply map mein daal do. Akhir me lenght return krdo.