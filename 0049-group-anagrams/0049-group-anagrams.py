class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for string in strs:
            sorted_string = ''.join(sorted(list(string)))
            
            if sorted_string in anagrams.keys():
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
        
        result = []
        for lists in anagrams.values():
            result.append(lists)
        
        return result