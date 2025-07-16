class Solution:
    def isValid(self, word: str) -> bool:
        # 1. Check minimum length
        if len(word) < 3:
            return False
        
        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False
        
        for c in word:
            # 2. Must be alphanumeric
            if not c.isalnum():
                return False
            
            # 3. Track vowels vs consonants for letters
            if c.isalpha():
                if c in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        
        # 4. At least one vowel AND one consonant
        return has_vowel and has_consonant
