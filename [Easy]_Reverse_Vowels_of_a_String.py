class Solution:
    def reverseVowels(self, s: str) -> str:
        def isvowel(ch):
            return ch in "aeiouAEIOU"

        s = list(s)  # strings are immutable, so convert to list
        n = len(s)
        i = 0
        j = n - 1

        while i < j:
            if not isvowel(s[i]):
                i += 1
            elif not isvowel(s[j]):
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
