class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        max_len = 0
        state = 0
        index_map = {0: -1}

        for i, ch in enumerate(s):
            if ch in vowel_to_bit:
                bit = vowel_to_bit[ch]
                state ^= (1 << bit)

            if state in index_map:
                max_len = max(max_len, i - index_map[state])
            else:
                index_map[state] = i

        return max_len
