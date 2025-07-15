class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0

        for i in sentences:
            word_count = 1 + i.count(" ")

            if word_count > max_count:
                max_count = word_count

        return max_count
