class Solution:
    def frequencySort(self, s: str) -> str:
        unique_ch = []
        freq_list = []

        # Count frequency of each unique character
        for i in s:
            if i not in unique_ch:
                count = 0
                for j in s:
                    if j == i:
                        count += 1
                unique_ch.append(i)
                freq_list.append(count)

        n = len(freq_list)

        # Sort using bubble sort (brute-force style)
        for i in range(n):
            for j in range(i + 1, n):
                if freq_list[j] > freq_list[i]:
                    freq_list[i], freq_list[j] = freq_list[j], freq_list[i]
                    unique_ch[i], unique_ch[j] = unique_ch[j], unique_ch[i]

        # Build the final string
        result = ""
        for i in range(n):
            result += unique_ch[i] * freq_list[i]

        return result
