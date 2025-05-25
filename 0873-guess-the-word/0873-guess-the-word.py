# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match_count(w1,w2):
            return sum(c1 == c2 for c1,c2 in zip(w1,w2))
        
        n = 0
        while n < 30:
            # frequency map of matches between words
            count = collections.Counter()
            for w1 in words:
                for w2 in words:
                    if w1 != w2:
                        # count matches
                        count[w1] += match_count(w1,w2)
            
            # choose word with max matches
            guess = max(words, key=lambda w: count[w])

            # get matches from master
            matches = master.guess(guess)
            if matches == 6:
                return
            
            # filter words based on matches
            words = [w for w in words if match_count(guess,w) == matches]
            n += 1