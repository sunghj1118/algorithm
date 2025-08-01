class Solution:
    def oddString(self, words: List[str]) -> str:
        def diffIntegerArray(word):
            arr = []
            
            for i in range(1, len(word)):
                arr.append(ord(word[i]) - ord(word[i-1]))
                
            return tuple(arr)
        
        diffArrays = {}
        for word in words:
            diffArray = diffIntegerArray(word)
            if diffArray in diffArrays:
                diffArrays[diffArray].append(word)
            else:
                diffArrays[diffArray] = [word]


        for diffArray in diffArrays:
            if len(diffArrays[diffArray]) == 1:
                return diffArrays[diffArray][0]

        return 