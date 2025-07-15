class Solution:
    def isValid(self, word: str) -> bool:
        if (len(word) < 3):
            return False
        
        vowels = set('aeiouAEIOU')
        hasVowel = False
        hasConsonant = False

        for char in word:
            if not char.isalnum():
                return False
            
            if char.isalpha():
                if char in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True
        
        return hasVowel and hasConsonant